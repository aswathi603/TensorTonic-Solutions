def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here
    min_val = min(values)
    max_val = max(values)

    # Handle edge case: all values are the same
    if min_val == max_val:
        return [0] * len(values)

    bin_width = (max_val - min_val) / num_bins
    bins = []

    for v in values:
        bin_index = int((v - min_val) / bin_width)

        # Ensure max value falls into the last bin
        if bin_index == num_bins:
            bin_index -= 1

        bins.append(bin_index)

    return bins