import numpy as np

def classification_metrics(y_true, y_pred, average="micro", pos_label=1):
    """
    Compute accuracy, precision, recall, F1 for single-label classification.
    Averages: 'micro' | 'macro' | 'weighted' | 'binary' (uses pos_label).
    Return dict with float values.
    """
    # Write code here
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    
    # Accuracy
    accuracy = np.mean(y_true == y_pred)
    
    classes = np.unique(np.concatenate([y_true, y_pred]))
    
    TP, FP, FN, support = {}, {}, {}, {}
    
    # Compute per-class stats
    for c in classes:
        TP[c] = np.sum((y_true == c) & (y_pred == c))
        FP[c] = np.sum((y_true != c) & (y_pred == c))
        FN[c] = np.sum((y_true == c) & (y_pred != c))
        support[c] = np.sum(y_true == c)
    
    def safe_div(a, b):
        return a / b if b != 0 else 0.0
    
    if average == "micro":
        tp = sum(TP.values())
        fp = sum(FP.values())
        fn = sum(FN.values())
        
        precision = safe_div(tp, tp + fp)
        recall = safe_div(tp, tp + fn)
        f1 = safe_div(2 * precision * recall, precision + recall)
    
    elif average == "macro":
        precisions, recalls, f1s = [], [], []
        
        for c in classes:
            p = safe_div(TP[c], TP[c] + FP[c])
            r = safe_div(TP[c], TP[c] + FN[c])
            f = safe_div(2 * p * r, p + r)
            
            precisions.append(p)
            recalls.append(r)
            f1s.append(f)
        
        precision = np.mean(precisions)
        recall = np.mean(recalls)
        f1 = np.mean(f1s)
    
    elif average == "weighted":
        total = len(y_true)
        precision = 0.0
        recall = 0.0
        f1 = 0.0
        
        for c in classes:
            w = support[c] / total
            p = safe_div(TP[c], TP[c] + FP[c])
            r = safe_div(TP[c], TP[c] + FN[c])
            f = safe_div(2 * p * r, p + r)
            
            precision += w * p
            recall += w * r
            f1 += w * f
    
    elif average == "binary":
        c = pos_label
        precision = safe_div(TP.get(c, 0), TP.get(c, 0) + FP.get(c, 0))
        recall = safe_div(TP.get(c, 0), TP.get(c, 0) + FN.get(c, 0))
        f1 = safe_div(2 * precision * recall, precision + recall)
    
    else:
        raise ValueError("Invalid average type")
    
    return {
        "accuracy": float(accuracy),
        "precision": float(precision),
        "recall": float(recall),
        "f1": float(f1)
    }