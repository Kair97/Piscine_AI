def mean(values):
    if not values:
        raise ValueError("Input list cannot be empty")
    return sum(values) / len(values)

def median(values):
    if not values:
        raise ValueError("Input list cannot be empty")
    sv = sorted(values)
    mid = len(sv) // 2
    if len(sv) % 2 == 0:
        return (sv[mid-1] + sv[mid]) / 2.0
    else:
        return sv[mid]
    
def variance(values):
    if not values:
        raise ValueError("Input list cannot be empty")
    m = mean(values)
    return sum((x-m)**2 for x in values) / len(values)

def mode(values):
    if not values:
        raise ValueError("Input list cannot be empty")

    
    counts = {}
    for x in values:
        counts[x] = counts.get(x, 0) + 1 

    max_count = max(counts.values()) 

    modes = [k for k,v in counts.items() if v == max_count]

    return min(modes)