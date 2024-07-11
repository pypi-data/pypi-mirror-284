import numpy as np
from ..core import Tensor
from .module import Module

def convolution2d(input: Tensor, weight: Tensor, bias: Tensor, stride: int, padding: int) -> Tensor:
    """
    Performs the 2D convolution operation using numpy's einsum for better performance.

    Args:
        input (Tensor): The input tensor.
        weight (Tensor): The weight tensor (filters).
        bias (Tensor): The bias tensor.
        stride (int): The stride of the convolution.
        padding (int): The size of the padding.

    Returns:
        Tensor: The result of the convolution.
    """
    # Pad the input if necessary
    if padding > 0:
        input_data = np.pad(input.data, ((0, 0), (0, 0), (padding, padding), (padding, padding)), mode='constant')
    else:
        input_data = input.data

    batch_size, in_channels, in_height, in_width = input_data.shape
    out_channels, _, kernel_height, kernel_width = weight.shape

    out_height = (in_height - kernel_height) // stride + 1
    out_width = (in_width - kernel_width) // stride + 1

    # Create a view of the input data with shape (batch_size, out_height, out_width, in_channels, kernel_height, kernel_width)
    input_strided = np.lib.stride_tricks.as_strided(
        input_data,
        shape=(batch_size, out_height, out_width, in_channels, kernel_height, kernel_width),
        strides=(input_data.strides[0], stride * input_data.strides[2], stride * input_data.strides[3],
                 input_data.strides[1], input_data.strides[2], input_data.strides[3])
    )

    # Perform the convolution using einsum
    output = np.einsum('bhwikl,oikl->bohw', input_strided, weight.data)

    # Add bias
    if bias is not None:
        output += bias.data.reshape(1, -1, 1, 1)

    return Tensor(output)


class _ConvNd(Module):
    """
    Base class for N-dimensional convolution layers.

    Args:
        in_channels (int): Number of channels in the input.
        out_channels (int): Number of channels produced by the convolution.
        kernel_size (int or tuple): Size of the convolving kernel.
        stride (int or tuple, optional): Stride of the convolution. Default: 1.
        padding (int or tuple, optional): Zero-padding added to both sides of the input. Default: 0.
        bias (bool, optional): If True, adds a learnable bias to the output. Default: True.
    """

    def __init__(self, in_channels, out_channels, kernel_size, stride=1, padding=0, bias=True):
        super().__init__()
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding
        self.weight = Tensor(self.xavier_init(out_channels, in_channels, kernel_size), requires_grad=True)
        if bias:
            self.bias = Tensor(np.zeros(out_channels), requires_grad=True)
        else:
            self.bias = None

    def xavier_init(self, out_channels, in_channels, kernel_size) -> np.ndarray:
        """
        Initializes the weights using the Xavier initialization method.

        Args:
            out_channels (int): Number of output channels.
            in_channels (int): Number of input channels.
            kernel_size (int or tuple): Size of the convolving kernel.

        Returns:
            np.ndarray: The initialized weights.
        """
        
        if isinstance(kernel_size, int):
            kernel_size = (kernel_size, kernel_size)
        
        fan_in = np.prod(kernel_size) * in_channels
        fan_out = np.prod(kernel_size) * out_channels

        limit = np.sqrt(6 / (fan_in + fan_out))

        return np.random.uniform(-limit, limit, (out_channels, in_channels, *kernel_size))

    def forward(self, input: Tensor) -> Tensor:
        raise NotImplementedError("forward method not implemented in base class")

class Conv2d(_ConvNd):
    """
    2D convolutional layer.

    Args:
        in_channels (int): Number of channels in the input.
        out_channels (int): Number of channels produced by the convolution.
        kernel_size (int or tuple): Size of the convolving kernel.
        stride (int or tuple, optional): Stride of the convolution. Default: 1.
        padding (int or tuple, optional): Zero-padding added to both sides of the input. Default: 0.
        bias (bool, optional): If True, adds a learnable bias to the output. Default: True.
    """

    def __init__(self, in_channels, out_channels, kernel_size, stride=1, padding=0, bias=True):
        super().__init__(in_channels, out_channels, kernel_size, stride, padding, bias)

    def forward(self, input: Tensor) -> Tensor:
        return convolution2d(input, self.weight, self.bias, self.stride, self.padding)

