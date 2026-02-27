'''
Question Link : https://www.tensortonic.com/problems/dot-product

Implement Dot Product
Linear Algebra
Easy
The dot product of two equal-length 1-D arrays 
x and y is the sum of the products of the corresponding elements. It can be calculated algebraically as:
 x⋅y=∑i=1nxi×yi where n is the length of the vectors, and xi and yi are the elements of x and y respectively.
 
and geometrically as:
 x⋅y=∥x∥⋅∥y∥⋅cos(θ) where ∥x∥ and ∥y∥ are the magnitudes of x and y, and θ is the angle between them.

Return the dot product as a scalar float.

Dot Produc



Examples
Input: x = [1,2,3], y = [4,5,6]
Output: 32.0
1 × 4 + 2 × 5 + 3 × 6 = 4 + 10 + 18 = 32

Input: x = [1,0], y = [0,1]
Output: 0.0
Orthogonal vectors (perpendicular)

Input: x = [-1,2], y = [3,-1]
Output: -5.0
(-1) × 3 + 2 × (-1) = -3 + (-2) = -5

Hint 1
Convert inputs to NumPy arrays first, then use vectorized operations.

Hint 2
NumPy has a built-in function for this:             np.dot(x, y).


Requirements
Must work for lists or NumPy arrays
Must return a float
Must be vectorized (no Python element loops)
Must handle 1D arrays only
Must raise ValueError for mismatched lengths
Constraints
Time limit: 200 ms, Memory: 64 MB
NumPy only (no sklearn, scipy)

'''


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