import math

def winsorize(values, lower_pct, upper_pct):
    """
    Clip values at the given percentile bounds.
    """
    # Write code here
    n = len(values)
    sorted_vals = sorted(values)

    def percentile(p):
        k = (n - 1) * p / 100
        f = int(k)
        c = f + 1 if f + 1 < n else f

        if f == c:
            return float(sorted_vals[f])

        return float(
            sorted_vals[f] +
            (k - f) * (sorted_vals[c] - sorted_vals[f])
        )

    lower_bound = percentile(lower_pct)
    upper_bound = percentile(upper_pct)

    result = []
    for v in values:
        if v < lower_bound:
            result.append(lower_bound)
        elif v > upper_bound:
            result.append(upper_bound)
        else:
            result.append(float(v))

    return result