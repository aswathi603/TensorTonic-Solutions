def target_encoding(categories, targets):
    """
    Replace each category with the mean target value for that category.
    """
    # Write code here
    if not categories or not targets or len(categories) != len(targets):
        return []

    sums = {}
    counts = {}

    for cat,tar in zip(categories , targets):
        sums[cat] = sums.get(cat,0) + tar
        counts[cat] = counts.get(cat,0) + 1

    means = {cat: sums[cat] / counts[cat] for cat in sums}

    return [means[cat] for cat in categories]