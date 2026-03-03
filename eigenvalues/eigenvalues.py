import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    # Write code here
    try:
        A = np.array(matrix)
    except Exception:
        return None

    # Must be a 2D square matrix
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        return None

    # Compute eigenvalues (supports real & complex)
    eigenvalues = np.linalg.eigvals(A)

    # Sort by real part, then imaginary part
    eigenvalues = np.array(
        sorted(eigenvalues, key=lambda x: (x.real, x.imag)),
        dtype=complex
    )

    return eigenvalues

