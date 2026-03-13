def interaction_features(X):
    """
    Generate pairwise interaction features and append them to the original features.
    """
    # Write code here
    if not X:
        return []

    n_features = len(X[0])
    result = []

    for row in X:
        new_row = list(row)

        for i in range(n_features):
            for j in range(i+1, n_features):
                new_row.append(row[i]*row[j])


        result.append(new_row)

    return result













