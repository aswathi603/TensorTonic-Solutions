import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    # Convert to numpy arrays (handles lists or arrays)
    x = np.array(x)
    y = np.array(y)
    
    # Compute distance
    return float(np.sqrt(np.sum((x - y) ** 2)))