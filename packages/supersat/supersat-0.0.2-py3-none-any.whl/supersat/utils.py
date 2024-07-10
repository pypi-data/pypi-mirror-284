import torch
from typing import Literal, Union
from collections import OrderedDict
from skimage.exposure import match_histograms


def activation(
    act_type: Literal['relu', 'lrelu', 'prelu'],
    inplace: bool = True,
    neg_slope: float = 0.05,
    n_prelu: int =1
) -> torch.nn.Module:
    """ This function creates an activation layer based 
    on the input type.

    Args:
        act_type (str): The type of activation layer.
        inplace (bool, optional): If the operation is inplace. Defaults 
            to True.
        neg_slope (float, optional): The negative slope for the
            LeakyReLU or PReLU activation layers. Defaults to 0.05.
        n_prelu (int, optional): The number of parameters for the
            PReLU activation layer. Defaults to 1.

    Returns:
        torch.nn.Module: The activation layer.
    """
    act_type = act_type.lower()
    
    if act_type == 'relu':
        layer = torch.nn.ReLU(inplace)
    
    if act_type == 'lrelu':
        layer = torch.nn.LeakyReLU(neg_slope, inplace)
    
    if act_type == 'prelu':
        layer = torch.nn.PReLU(num_parameters=n_prelu, init=neg_slope)

    return layer


def sequential(
    *args: Union[torch.nn.Module, torch.nn.Sequential]
) -> torch.nn.Sequential:
    """
    Create a Sequential container from the provided modules.

    Modules will be added to the Sequential container in the order they
    are passed. If an nn.Sequential container is passed as an argument,
    its child modules will be unpacked and added individually.

    Args:
        args (nn.Module or nn.Sequential): Variable number of modules to be
            added to the Sequential container. Modules can be instances of
            nn.Module or nested nn.Sequential containers.

    Raises:
        NotImplementedError: If an OrderedDict is passed as the single 
            argument.
    
    Returns:
        nn.Sequential: A Sequential container comprising the provided
            modules in the order given.
    """
    
    # Check if only a single argument is passed
    if len(args) == 1:
        # Raise an error if the argument is an OrderedDict
        if isinstance(args[0], OrderedDict):
            raise NotImplementedError(
                'sequential does not support OrderedDict input.')
        # Return the argument directly if it is not an OrderedDict
        return args[0]
    
    modules = []
    
    # Iterate through the provided arguments
    for module in args:
        if isinstance(module, torch.nn.Sequential):
            # Unpack and add child modules if the argument is a Sequential container
            modules.extend(module.children())
        elif isinstance(module, torch.nn.Module):
            # Add the module directly if it is an instance of nn.Module
            modules.append(module)

    # Create and return a Sequential container with the collected modules
    return torch.nn.Sequential(*modules)


def hq_histogram_matching(image1: torch.Tensor, image2: torch.Tensor) -> torch.Tensor:
    """ Lazy implementation of histogram matching 

    Args:
        image1 (torch.Tensor): The low-resolution image (C, H, W).
        image2 (torch.Tensor): The super-resolved image (C, H, W).

    Returns:
        torch.Tensor: The super-resolved image with the histogram of
            the target image.
    """

    # Go to numpy
    np_image1 = image1.detach().cpu().numpy()
    np_image2 = image2.detach().cpu().numpy()

    if np_image1.ndim == 3:
        np_image1_hat = match_histograms(np_image1, np_image2, channel_axis=0)
    elif np_image1.ndim == 2:
        np_image1_hat = match_histograms(np_image1, np_image2, channel_axis=None)
    else:
        raise ValueError("The input image must have 2 or 3 dimensions.")

    # Go back to torch
    image1_hat = torch.from_numpy(np_image1_hat).to(image1.device)

    return image1_hat