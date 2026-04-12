def mean_rating_imputation(ratings_matrix, mode):
    """
    Fill missing ratings (zeros) with user or item means.
    """
    # Write code here
    # Copy matrix (to avoid modifying original)
    result = [row[:] for row in ratings_matrix]
    
    n = len(ratings_matrix)
    m = len(ratings_matrix[0]) if n > 0 else 0
    
    if mode == "user":
        for i in range(n):
            # Get non-zero values in row
            values = [x for x in ratings_matrix[i] if x != 0]
            
            # Compute mean (avoid division by zero)
            mean = sum(values) / len(values) if values else 0
            
            # Fill missing values
            for j in range(m):
                if result[i][j] == 0:
                    result[i][j] = float(mean)
    
    elif mode == "item":
        for j in range(m):
            # Get non-zero values in column
            values = [ratings_matrix[i][j] for i in range(n) if ratings_matrix[i][j] != 0]
            
            mean = sum(values) / len(values) if values else 0
            
            # Fill missing values
            for i in range(n):
                if result[i][j] == 0:
                    result[i][j] = float(mean)
    
    return result