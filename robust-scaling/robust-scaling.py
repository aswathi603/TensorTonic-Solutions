def robust_scaling(values):
    """
    Scale values using median and IQR (Q3 - Q1).
    """
    # Write code here
    n = len(values)

    # Single element case
    if n == 1:
        return [0.0]

    # Sort values
    sorted_vals = sorted(values)

    # Helper to compute median
    def median(arr):
        m = len(arr)
        mid = m // 2
        if m % 2 == 0:
            return (arr[mid - 1] + arr[mid]) / 2
        else:
            return arr[mid]

    # Compute median
    med = median(sorted_vals)

    # Split into lower and upper halves
    if n % 2 == 0:
        lower = sorted_vals[:n // 2]
        upper = sorted_vals[n // 2:]
    else:
        lower = sorted_vals[:n // 2]
        upper = sorted_vals[n // 2 + 1:]

    # Compute Q1 and Q3
    q1 = median(lower)
    q3 = median(upper)

    iqr = q3 - q1

    # Apply robust scaling
    if iqr == 0:
        return [float(x - med) for x in values]
    else:
        return [((x - med) / iqr) for x in values]
