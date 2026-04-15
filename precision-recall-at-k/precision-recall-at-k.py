import numpy as np

def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    relevant_set = set(relevant)
    
    # Top-k items
    top_k = recommended[:k]
    
    # Count hits
    hits = sum(1 for item in top_k if item in relevant_set)
    
    # Precision
    precision = hits / k if k > 0 else 0.0
    
    # Recall
    recall = hits / len(relevant_set) if relevant_set else 0.0
    
    return [float(precision), float(recall)]