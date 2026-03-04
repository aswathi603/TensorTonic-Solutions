def rank_transform(values):
    """
    Replace each value with its average rank.
    """
    # Write code here
    if not values:
        return []
    sort_vals = sorted(values)
    ranks = {}

    i = 0
    n = len(sort_vals)

    while i < n:
        j = i 

        while j < n and sort_vals[j] == sort_vals[i]:
            j+=1

        avgRank = (i+1+j)/2
        ranks[sort_vals[i]] = avgRank

        i = j

    return [ranks[val] for val in values]









