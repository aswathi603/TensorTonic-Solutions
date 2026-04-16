import numpy as np

def roc_curve(y_true, y_score):
    """
    Compute ROC curve from binary labels and scores.
    Returns: (fpr, tpr, thresholds)
    """
    # Write code here
    
    y_true = np.asarray(y_true)
    y_score = np.asarray(y_score)
    
    # Sort by descending score
    desc_idx = np.argsort(-y_score)
    y_true = y_true[desc_idx]
    y_score = y_score[desc_idx]
    
    # Total positives and negatives
    P = np.sum(y_true == 1)
    N = np.sum(y_true == 0)
    
    # Cumulative TP and FP
    tp = np.cumsum(y_true == 1)
    fp = np.cumsum(y_true == 0)
    
    # Find indices where score changes (unique thresholds)
    distinct_idxs = np.where(np.diff(y_score))[0]
    threshold_idxs = np.r_[distinct_idxs, len(y_score) - 1]
    
    # Select TP/FP at those points
    tp = tp[threshold_idxs]
    fp = fp[threshold_idxs]
    thresholds = y_score[threshold_idxs]
    
    # Compute TPR and FPR
    tpr = tp / P if P > 0 else np.zeros_like(tp, dtype=float)
    fpr = fp / N if N > 0 else np.zeros_like(fp, dtype=float)
    
    # Add starting point (0,0) with threshold = inf
    tpr = np.r_[0.0, tpr]
    fpr = np.r_[0.0, fpr]
    thresholds = np.r_[np.inf, thresholds]
    
    return fpr.tolist(), tpr.tolist(), thresholds.tolist()