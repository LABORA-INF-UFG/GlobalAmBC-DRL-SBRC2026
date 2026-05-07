# ============================================================
# Utility Functions
# ============================================================

import numpy as np


def normalize(data):
    """
    Normalize input values to the [0,1] range.

    Parameters:
        data (array-like):
            Input values to be normalized.

    Returns:
        np.ndarray:
            Normalized values.
    """
    return (data - np.min(data)) / (np.max(data) - np.min(data))