from typing import Optional
import torch
from torch.nn import Module, DataParallel
from .buffering import Buffer as Buffering


class Buffer(torch.Tensor):
    def __init__(self, tensor: Optional[torch.Tensor], persistent: bool = True): ...

Buffer = Buffering
del Buffering

import torch.nn
torch.nn.Buffer = Buffer


def refine_model(model: Module):
    if isinstance(model, DataParallel) or isinstance(model, torch.nn.parallel.DistributedDataParallel):
        return model.module
    else:
        return model