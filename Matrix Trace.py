'''
Question Link : https://www.tensortonic.com/problems/matrix-trace

Matrix Trace
Linear Algebra
Easy
Compute the trace of a square matrix, defined as the sum of its diagonal elements.

Mathematical Definition
Trace of Matrix A:
                                tr(A)= i=1  n∑ a(ii)

where aii are the diagonal elements of matrix AA.

Function Arguments
A: 2D NumPy array, shape (N, N) - square matrix
Matrix Trace
Sum of Diagonal Elements


4      3    -2
-1     5     1
2      0     6

tr(A)=4+5+6=15


4
Examples
Input: A = [[1, 2], [3, 4]]
Output: 5

Input: A = [[2, -1, 0], [3, 5, 1], [0, 2, -2]]
Output: 5 (trace = 2 + 5 + (-2))

Input: A = [[42]]
Output: 42

Hint 1
Hint 2
Requirements
Return a single scalar (float or int)
Do not use np.trace() or A.diagonal().sum()
Compute manually via indexing or iteration
Handle negative, zero, and float elements
Handle 1x1 edge case
Constraints
1 ≤ N ≤ 1000
Matrix elements can be any float or int
Time limit: 100ms

'''

import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    trace_sum = 0
    for i in range(len(A)):
        trace_sum += A[i][i]
    return trace_sum