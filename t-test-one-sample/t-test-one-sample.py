import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    # Write code here
# Convert input to a numpy array for vector operations
    data = np.array(x)
    
    # Calculate sample size (n)
    n = len(data)
    
    # Calculate sample mean (x_bar)
    x_bar = np.mean(data)
    
    # Calculate sample standard deviation (s) with Bessel correction (ddof=1)
    s = np.std(data, ddof=1)
    
    # Calculate the t-statistic
    # t = (x_bar - mu0) / (s / sqrt(n))
    t_stat = (x_bar - mu0) / (s / np.sqrt(n))
    
    return float(t_stat)