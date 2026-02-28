'''
Expected Value (Discrete Distribution)
Probability and Statistics
Easy
Compute the expected value of a discrete random variable given its values and probabilities.

Mathematical Definition
Expected Value:
E[X]= i=0∑N−1 xi pi 

where xi are the values and pi are their corresponding probabilities with ∑pi=1.

Function Arguments
x: array-like, shape (N,) - possible values
p: array-like, shape (N,) - corresponding probabilities

Examples
Input: x = [1, 2, 3], p = [0.2, 0.5, 0.3]

Output: E[X] = 2.1

Input: x = [1, 2, 3, 4], p = [0.25, 0.25, 0.25, 0.25]

Output: E[X] = 2.5

Hint 1
Hint 2
Requirements
Raise a ValueError if probabilities don't sum to 1 (within tolerance 10−6) - any error message is accepted
Ensure shapes of x and p match
Return a single float
Constraints
1 ≤ N ≤ 10,000
NumPy only
Time limit: 200ms

'''


import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x = np.asarray(x , dtype = float)
    p = np.asarray(p , dtype = float)

    if x.shape != p.shape:
        raise ValueError("x and p must have same shape")

    if not np.isclose(p.sum(), 1.0, atol = 1e-6):
        raise ValueError("Probabilities must sum to 1")

    return float(np.sum(x*p))