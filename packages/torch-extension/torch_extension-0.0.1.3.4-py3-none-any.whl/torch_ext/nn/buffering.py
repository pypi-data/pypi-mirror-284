from typing import Optional
import ctypes
import inspect
import torch
from torch import nn


class _BufferingModule:
    # This class instance will replace the `nn.Module` instance `self` in the `register_parameter` when registering a buffer,
    # while the `self` in the `__setattr__` will keep same.
    class FakeDict:
        def __setitem__(self, _, __): pass
    def __init__(self):
        self._parameters = _BufferingModule.FakeDict()


class _BufferingFakeDict:
    # This class instance will replace the global variable `_global_parameter_registration_hooks` in the `register_parameter`
    # when registering a buffer, and the returns a iterator when `values()` is called. When iterating, the original
    # `_global_parameter_registration_hooks` will be restored.
    class Iterator:
        def __init__(self, frame, global_parameter_registration_hooks):
            self.frame = frame
            self.global_parameter_registration_hooks = global_parameter_registration_hooks
            
        def __iter__(self):
            return self
    
        def __next__(self):
            # Retore the original `_global_parameter_registration_hooks`.
            self.frame.f_globals['_global_parameter_registration_hooks'] = self.global_parameter_registration_hooks
            ctypes.pythonapi.PyFrame_LocalsToFast(ctypes.py_object(self.frame), ctypes.c_int(0))
            raise StopIteration
    
    def __init__(self, frame, global_parameter_registration_hooks):
        self.frame = frame
        self.global_parameter_registration_hooks = global_parameter_registration_hooks
    
    def values(self):
        return _BufferingFakeDict.Iterator(self.frame, self.global_parameter_registration_hooks)


def self_from_frame(frame):
    '''
    Get the `self` instance of the frame if the frame is a called method, else `None` will be returned.
    '''
    co_varnames = frame.f_code.co_varnames
    if len(co_varnames) > 0:
        module_self = co_varnames[0]
        module_self: nn.Module = frame.f_locals[module_self]
        func_name = frame.f_code.co_name
        if hasattr(module_self, func_name) and frame.f_back.f_locals.get(func_name) is None:
            return module_self


class _ParameterizedBuffer:
    def __init__(self, tensor: Optional[torch.Tensor], persistent: bool = True):
        super().__setattr__('__tensor', tensor)
        super().__setattr__('__persistent', persistent)
    
    def __getattr__(self, name: str):
        if name == 'grad_fn':
            # The attibute `grad_fn` is called by `register_parameter` method, so it can be replaced by this getter to
            # insert any operations, which ignores the storage in `register_parameter` as a parameter, instaed, `register_buffer`
            # will be called here.
            stack= inspect.stack()
            if len(stack) > 2 and (stack[1].function == 'register_parameter' and stack[2].function == '__setattr__'):
                # Only if the last frame function is `register_parameter` and the last second frame fuction is `__setattr__`, 
                # which means it is in the parameterized hook process, this buffer storage will be called, else `grad_fn`
                # will be gotten normally.
                last_frame = stack[1].frame
                module_self: nn.Module = self_from_frame(last_frame)
                if module_self is not None and isinstance(module_self, nn.Module):
                    co_varnames = last_frame.f_code.co_varnames
                    if len(co_varnames) > 1:
                        last_self_name = co_varnames[0]
                        last_name = last_frame.f_locals[co_varnames[1]]
                        
                        last_frame.f_locals[last_self_name] = _BufferingModule()
                        global_parameter_registration_hooks = last_frame.f_globals['_global_parameter_registration_hooks']
                        last_frame.f_globals['_global_parameter_registration_hooks'] = _BufferingFakeDict(last_frame, global_parameter_registration_hooks)
                        ctypes.pythonapi.PyFrame_LocalsToFast(ctypes.py_object(last_frame), ctypes.c_int(0))
                        
                        module_self.register_buffer(last_name, super().__getattribute__('__tensor'), super().__getattribute__('__persistent'))
                        return False
        try:
            # Find through the buffer instance itself.
            attr = super().__getattribute__(name)
        except AttributeError:
            # If the attribute cannot be accessed by the instance itself, it will be gotten by the stored tensor.
            attr = super().__getattribute__('__tensor').__getattribute__(name)
        return attr
    
    def __setattr__(self, name: str, value):
        if name == '__class__':
            # Only the attribute `__class__` is required to set using the property setter.
            super().__setattr__(name, value)
        else:
            # All other attributes should be set in the stored tensor.
            super().__getattribute__('__tensor').__setattr__(name, value)
    
    def __repr__(self) -> str:
        return f"<unregistered buffer of {super().__getattribute__('__tensor').__repr__()}>"
    
    @property
    def __class__(self):
        stack= inspect.stack()
        stack_length = len(stack)
        owner_class = None
        if (stack_length > 2 and stack[2].function == '__setattr__' or 
            (stack_length > 3 and stack[2].function == 'register_parameter' and stack[3].function == '__setattr__')):
            # Consider the current frame function is `__instancecheck__`, if the last frame function is `__setattr__`,
            # or the last frame function is `register_parameter` and the last second frame function is `__setattr__`,
            # that means it is in the parameterized hook process.
            frame = stack[2].frame
            module_self: nn.Module = self_from_frame(frame)
            owner_class = super().__getattribute__('__tensor').__class__
            if module_self is not None and isinstance(module_self, nn.Module) and issubclass(owner_class, torch.Tensor):
                # When the `__class__` of the stored tensor is `torch.Tensor` or its subclass, returning the `nn.Parameter`
                # to hook the `__instancecheck__`.
                return nn.Parameter
        elif stack_length > 1 and stack[1].function == 'register_buffer':
            # When the buffer is passed to the `register_buffer` method, the stored tensor and its persistent status will
            # be extracted into the `register_buffer` method. (Strangely, the `__instancecheck__` is not called, so the
            # stack index is less.)
            frame = stack[1].frame
            module_self: nn.Module = self_from_frame(frame)
            if module_self is not None and isinstance(module_self, nn.Module):
                co_varnames = frame.f_code.co_varnames
                if len(co_varnames) > 3:
                    from pyreflex import get_instruction_at
                    tensor_name = co_varnames[2]
                    persistent_name = co_varnames[3]
                    lasti = frame.f_back.f_lasti
                    call_instruction = get_instruction_at(frame.f_back.f_code, lasti)
                    if call_instruction.argval <= 2:
                        # Only when explicitly passing the `persistent` argument to the method `register_buffer`, the passed
                        # one will be applied, otherwise the `persistent` attribute in the buffer instance will be exploited.
                        frame.f_locals[persistent_name] = super().__getattribute__('__persistent')
                        ctypes.pythonapi.PyFrame_LocalsToFast(ctypes.py_object(frame), ctypes.c_int(0))
                    frame.f_locals[tensor_name] = super().__getattribute__('__tensor')
                    ctypes.pythonapi.PyFrame_LocalsToFast(ctypes.py_object(frame), ctypes.c_int(0))
        return owner_class if owner_class is not None else super().__getattribute__('__tensor').__class__
    
    @__class__.setter
    def __class__(self, value):
        # The `__class__` should be set through the stored tensor.
        super().__getattribute__('__tensor').__class__ = value


class Buffer(_ParameterizedBuffer): pass