import numpy as np

def kfold_split(N, k, shuffle=True, rng=None):
    """
    Returns: list of length k with tuples (train_idx, val_idx)
    """
    # Write code here
    # Step 1: Create indices
    indices = np.arange(N)
    
    # Step 2: Shuffle if needed
    if shuffle:
        if rng is not None:
            indices = rng.permutation(indices)
        else:
            np.random.shuffle(indices)
    
    # Step 3: Compute fold sizes
    fold_sizes = [N // k] * k
    for i in range(N % k):
        fold_sizes[i] += 1
    
    # Step 4: Split into folds
    folds = []
    current = 0
    
    for size in fold_sizes:
        val_idx = indices[current:current + size]
        
        train_idx = np.concatenate((
            indices[:current],
            indices[current + size:]
        ))
        
        folds.append((train_idx, val_idx))
        current += size
    
    return folds
