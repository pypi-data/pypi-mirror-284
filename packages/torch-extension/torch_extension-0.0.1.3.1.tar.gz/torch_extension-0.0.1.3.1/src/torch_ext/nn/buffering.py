from typing import Optional
import ctypes
import inspect
import torch
from torch import nn


class _BufferingModule:
    class FakeDict:
        def __setitem__(self, _, __): pass
    def __init__(self):
        self._parameters = _BufferingModule.FakeDict()


class _BufferingFakeDict:
    class Iterator:
        def __init__(self, frame, global_parameter_registration_hooks):
            self.frame = frame
            self.global_parameter_registration_hooks = global_parameter_registration_hooks
            
        def __iter__(self):
            return self
    
        def __next__(self):
            self.frame.f_globals['_global_parameter_registration_hooks'] = self.global_parameter_registration_hooks
            ctypes.pythonapi.PyFrame_LocalsToFast(ctypes.py_object(self.frame), ctypes.c_int(0))
            raise StopIteration
    
    def __init__(self, frame, global_parameter_registration_hooks):
        self.frame = frame
        self.global_parameter_registration_hooks = global_parameter_registration_hooks
    
    def values(self):
        return _BufferingFakeDict.Iterator(self.frame, self.global_parameter_registration_hooks)


def self_from_frame(frame):
    co_varnames = frame.f_code.co_varnames
    if len(co_varnames) > 0:
        module_self = co_varnames[0]
        module_self: nn.Module = frame.f_locals[module_self]
        func_name = frame.f_code.co_name
        if hasattr(module_self, func_name) and frame.f_back.f_locals.get(func_name) is None:
            return module_self


class _BufferDescriptor:
    def __get__(self, obj, type=None):
        stack= inspect.stack()
        stack_length = len(stack)
        i = 1
        if stack_length > i and stack[1].function == '__getattr__':
            i += 1
        if stack_length > i and stack[i].function == 'register_parameter':
            last_frame = stack[i].frame
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
                    
                    module_self.register_buffer(last_name, getattr(obj, '__tensor'), getattr(obj, '__persistent'))
        return False


class _ParameterizedBuffer:
    __buffer_descriptor = _BufferDescriptor()
    
    def __init__(self, tensor: Optional[torch.Tensor]) -> None:
        super().__setattr__('__tensor', tensor)
        super().__setattr__('__is_module_class', True)
        super().__setattr__('__class', torch.Tensor)
    
    def __getattr__(self, name: str):
        if name == 'grad_fn':
            stack= inspect.stack()
            if len(stack) > 1 and stack[1].function == 'register_parameter':
                module_self = self_from_frame(stack[1].frame)
                if module_self is not None and isinstance(module_self, nn.Module):
                    return self.__buffer_descriptor
        try:
            attr = super().__getattribute__(name)
        except AttributeError:
            attr = super().__getattribute__('__tensor').__getattribute__(name)
        return attr
    
    def __setattr__(self, name: str, value):
        if name == '__class__':
            super().__setattr__(name, value)
        else:
            super().__getattribute__('__tensor').__setattr__(name, value)
    
    def __repr__(self) -> str:
        return f"<unregistered buffer of {super().__getattribute__('__tensor').__repr__()}>"
    
    @property
    def __class__(self):
        stack= inspect.stack()
        stack_length = len(stack)
        i = 1
        if stack_length > i and stack[i].function == '__instancecheck__':
            i += 1
        if stack_length > i and (stack[i].function == '__setattr__' or stack[i].function == 'register_parameter'):
            frame = stack[i].frame
            module_self: nn.Module = self_from_frame(frame)
            if module_self is not None and isinstance(module_self, nn.Module) and getattr(self, '__is_module_class', False):
                return nn.Parameter
        return super().__getattribute__('__class')
    
    @__class__.setter
    def __class__(self, value):
        super().__setattr__('__class', value)
        stack = inspect.stack()
        if len(stack) > 2:
            module_self: nn.Module = self_from_frame(frame = stack[2].frame)
            if module_self is not None and isinstance(module_self, nn.Module):
                if value is torch.Tensor:
                    super().__setattr__('__is_module_class', True)
                elif getattr(self, '__is_module_class', False):
                    super().__delattr__('__is_module_class')


class Buffer(_ParameterizedBuffer):
    def __init__(self, tensor: Optional[torch.Tensor], persistent: bool = True):
        super().__init__(tensor)
        super(_ParameterizedBuffer, self).__setattr__('__persistent', persistent)