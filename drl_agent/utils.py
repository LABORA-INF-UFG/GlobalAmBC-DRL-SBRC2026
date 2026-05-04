import numpy as np

def normalize(data):
    """
    Normalize input values to a standard range.

    Parameters:
        x (float): input value

    Returns:
        float: normalized value
    """
    return (data - np.min(data)) / (np.max(data) - np.min(data))