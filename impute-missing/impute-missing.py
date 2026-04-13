import numpy as np

def impute_missing(X, strategy='mean'):
    """
    Fill NaN values in each feature column using column mean or median.
    """
    # Write code here
    # Convert to numpy array (float for NaN support)
    X = np.array(X, dtype=float)
    
    # Handle 1D case
    if X.ndim == 1:
        X = X.reshape(-1, 1)
        squeeze_back = True
    else:
        squeeze_back = False
    
    result = X.copy()
    
    # Compute statistic
    if strategy == 'mean':
        stat = np.nanmean(result, axis=0)
    elif strategy == 'median':
        stat = np.nanmedian(result, axis=0)
    else:
        raise ValueError("Strategy must be 'mean' or 'median'")
    
    # Replace NaN stats (all-NaN columns) with 0
    stat = np.where(np.isnan(stat), 0, stat)
    
    # Find NaN positions
    nan_mask = np.isnan(result)
    
    # Replace NaNs using broadcasting
    result[nan_mask] = np.take(stat, np.where(nan_mask)[1])
    
    # Return in original shape
    if squeeze_back:
        return result.flatten()
    
    return result