import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    """
    Normalize a 2D matrix along specified axis using specified norm.
    """
    # Write code here
    try:
        A = np.array(matrix, dtype=float)

        # Validate 2D input
        if A.ndim != 2:
            return None

        # Compute norms based on type
        if norm_type == 'l2':
            norms = np.sqrt(np.sum(A ** 2, axis=axis, keepdims=True))
        elif norm_type == 'l1':
            norms = np.sum(np.abs(A), axis=axis, keepdims=True)
        elif norm_type == 'max':
            norms = np.max(np.abs(A), axis=axis, keepdims=True)
        else:
            return None

        # Avoid division by zero
        norms[norms == 0] = 1

        return A / norms

    except Exception:
        return None