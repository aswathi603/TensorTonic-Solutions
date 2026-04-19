import numpy as np

def linear_regression_closed_form(X, y):
    """
    Compute the optimal weight vector using the normal equation.
    """
    # Write code here
    # Convert to numpy arrays
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)
    
    # Ensure y is column vector
    if y.ndim == 1:
        y = y.reshape(-1, 1)
    
    # Normal equation
    Xt = X.T
    XtX = Xt @ X
    XtX_inv = np.linalg.inv(XtX)
    Xt_y = Xt @ y
    
    w = XtX_inv @ Xt_y
    
    # Return as 1D array
    return w.flatten()