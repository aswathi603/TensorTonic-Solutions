import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    # Write code here
    # Convert to numpy array
    A = np.array(A, dtype=float)
    
    # Step 1: Check if 2D
    if A.ndim != 2:
        return None
    
    # Step 2: Check if square
    n, m = A.shape
    if n != m:
        return None
    
    # Step 3: Check if singular (determinant ≈ 0)
    det = np.linalg.det(A)
    if abs(det) < 1e-10:
        return None
    
    # Step 4: Compute inverse
    A_inv = np.linalg.inv(A)
    
    return A_inv
