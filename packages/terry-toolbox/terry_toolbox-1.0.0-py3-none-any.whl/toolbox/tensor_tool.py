import numpy as np
import torch


def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    if isinstance(vector, np.ndarray):
        return vector / np.linalg.norm(vector)
    elif isinstance(vector, torch.Tensor):
        return vector / torch.norm(vector)
    else:
        raise TypeError("vector should be either numpy.ndarray or torch.Tensor")