from typing import overload, Optional
import torch

class Buffer(torch.Tensor):
    @overload
    def __init__(self, tensor: Optional[torch.Tensor], persistent: bool = True): ...