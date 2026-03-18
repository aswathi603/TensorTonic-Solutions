import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    # Validate 1D vectors and equal length
    if x.ndim != 1 or y.ndim != 1 or x.shape[0] != y.shape[0]:
        raise ValueError("Vectors must be 1D and of equal length")

    return float(np.sum(x * y))