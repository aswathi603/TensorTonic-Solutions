def frequency_encoding(values):
    """
    Replace each value with its frequency proportion.
    """
    # Write code here
    if not values:
        return []

    freq = {}
    n = len(values)

    for val in values:
        freq[val] = freq.get(val,0)+1

    return [freq[val] / n for val in values]
