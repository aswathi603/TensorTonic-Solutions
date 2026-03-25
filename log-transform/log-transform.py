import math
def log_transform(values):
    """
    Apply the log1p transformation to each value.
    """
    # Write code here
    result = []
    
    for x in values:
        # Apply log(1 + x)
        transformed_value = math.log1p(x)
        
        # Round to 4 decimal places (as seen in examples)
        result.append(round(transformed_value, 4))
    
    return result