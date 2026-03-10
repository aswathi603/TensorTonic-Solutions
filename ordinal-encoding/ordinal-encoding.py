def ordinal_encoding(values, ordering):
    """
    Encode categorical values using the provided ordering.
    """
    # Write code here
    # Step 1: Build mapping (value -> rank)
    mapping = {value: index for index, value in enumerate(ordering)}

    # Step 2: Encode values using the mapping
    return [mapping[val] for val in values]