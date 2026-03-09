import numpy as np

def pearson_correlation(X):
    """
    Compute Pearson correlation matrix from dataset X.
    """
    # Write code here
    X = np.asarray(X,dtype = float)

    X_centered  = X - np.mean(X,axis = 0)

    cov_matrix = np.dot(X_centered.T,X_centered) / (X.shape[0] - 1 )

    std_dev = np.sqrt(np.diag(cov_matrix))

    corr_matrix = cov_matrix / np.outer(std_dev,std_dev)

    return corr_matrix