import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    
    # Convert to numpy array
    X = np.array(X, dtype=float)
    
    # Step 1: Validate input
    if X.ndim != 2:
        return None
    
    N, D = X.shape
    
    if N < 2:
        return None
    
    # Step 2: Compute mean
    mu = np.mean(X, axis=0)
    
    # Step 3: Center data
    X_centered = X - mu
    
    # Step 4: Compute covariance matrix
    cov_matrix = (X_centered.T @ X_centered) / (N - 1)
    
    return cov_matrix
    