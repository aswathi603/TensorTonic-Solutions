import numpy as np

def confusion_matrix_norm(y_true, y_pred, num_classes=None, normalize='none'):
    """
    Compute confusion matrix with optional normalization.
    """
    # Write code here
    y_true = np.asarray(y_true, dtype=int)
    y_pred = np.asarray(y_pred, dtype=int)
    
    # Handle empty input
    if y_true.size == 0:
        K = num_classes if num_classes is not None else 0
        return np.zeros((K, K), dtype=float if normalize != 'none' else int)
    
    # Infer number of classes
    if num_classes is None:
        K = max(y_true.max(), y_pred.max()) + 1
    else:
        K = num_classes
    
    # Validate labels
    if (y_true < 0).any() or (y_pred < 0).any() or \
       (y_true >= K).any() or (y_pred >= K).any():
        raise ValueError("Labels out of valid range [0, K-1]")
    
    # Compute confusion matrix via bincount
    indices = y_true * K + y_pred
    counts = np.bincount(indices, minlength=K*K)
    C = counts.reshape(K, K)
    
    # No normalization
    if normalize == 'none':
        return C
    
    C = C.astype(float)
    eps = 1e-12
    
    if normalize == 'true':
        row_sums = C.sum(axis=1, keepdims=True)
        row_sums[row_sums == 0] = 1.0
        return C / (row_sums + eps)
    
    elif normalize == 'pred':
        col_sums = C.sum(axis=0, keepdims=True)
        col_sums[col_sums == 0] = 1.0
        return C / (col_sums + eps)
    
    elif normalize == 'all':
        total = C.sum()
        if total == 0:
            return C
        return C / total
    
    else:
        raise ValueError("normalize must be 'none', 'true', 'pred', or 'all'")