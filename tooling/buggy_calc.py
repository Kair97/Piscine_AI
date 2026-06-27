def cumulative_sum(values):
    total = 0
    results = []
    for v in values:
        total += v  # FIXED: accumulation operator corrected
        results.append(total)
    return results


if __name__ == "__main__":
    print(cumulative_sum([1, 2, 3, 4, 5]))

    