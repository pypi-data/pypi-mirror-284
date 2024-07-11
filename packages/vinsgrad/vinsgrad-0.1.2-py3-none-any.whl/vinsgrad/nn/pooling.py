import numpy as np
from ..core import Tensor
from .module import Module
from ..utils.utils import argmax

def max_pool2d(input: Tensor, kernel_size: int, stride: int, padding: int):
    """
    Performs the 2d max pooling operation.
    
    Args:
        input (Tensor): The input tensor.
        kernel_size (int): The size of the max pooling window.
        stride (int): The stride of the max pooling.
        padding (int): The padding of the max pooling.
    
    Returns:
        Tensor: The result of the max pooling operation.
    """
    batch_size, channels, height, width = input.shape
    
    # Apply padding if necessary
    if padding > 0:
        input = input.pad(((0, 0), (0, 0), (padding, padding), (padding, padding)), mode='constant')
    
    # Calculate output dimensions
    out_height = (height + 2 * padding - kernel_size) // stride + 1
    out_width = (width + 2 * padding - kernel_size) // stride + 1
    
    # Initialize output tensor
    output = Tensor(np.zeros((batch_size, channels, out_height, out_width)))
    
    # Perform max pooling
    for i in range(out_height):
        for j in range(out_width):
            h_start = i * stride
            h_end = h_start + kernel_size
            w_start = j * stride
            w_end = w_start + kernel_size
            pool_region = input[:, :, h_start:h_end, w_start:w_end]
            max_values = pool_region.max(axis=(2, 3))
            output[:, :, i, j] = max_values
    
    return output

class _MaxPoolNd(Module):
    """
    Base class for N-dimensional max pooling layers.

    Args:
        kernel_size (int or tuple): Size of the pooling kernel.
        stride (int or tuple, optional): Stride of the pooling. Default: 1.
        padding (int or tuple, optional): Zero-padding added to both sides of the input. Default: 0.
    """

    def __init__(self, kernel_size, stride=None, padding=0):
        super(_MaxPoolNd, self).__init__()
        self.kernel_size = kernel_size
        self.stride = stride if stride is not None else kernel_size
        self.padding = padding

    def forward(self, input: Tensor):
        raise NotImplementedError("forward method not implemented in base class")
    
class MaxPool2d(_MaxPoolNd):
    """
    2D max pooling layer.

    Args:
        kernel_size (int or tuple): Size of the pooling kernel.
        stride (int or tuple, optional): Stride of the pooling. Default: 1.
        padding (int or tuple, optional): Zero-padding added to both sides of the input. Default: 0.
    """

    def __init__(self, kernel_size, stride=1, padding=0):
        super(MaxPool2d, self).__init__(kernel_size, stride, padding)

    def forward(self, input: Tensor):
        return max_pool2d(input, self.kernel_size, self.stride, self.padding)
