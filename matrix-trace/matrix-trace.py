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

