import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    
    # PMF (vectorized)
    pmf = x * p + (1 - x) * (1 - p)
    
    # Mean and Variance
    mean = float(p)
    var = float(p * (1 - p))
    
    return pmf, mean, var