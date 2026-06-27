# stats.py
"""Statistical analysis module containing mathematical operations."""

VERSION: str = "1.0"


def mean(values: list[float]) -> float:
    if not values:
        raise ValueError("The list cannot be empty.")
    return sum(values) / len(values)


def median(values: list[float]) -> float:
    if not values:
        raise ValueError("The list cannot be empty.")
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2
    return sorted_vals[mid]


def variance(values: list[float]) -> float:
    if not values:
        raise ValueError("The list cannot be empty.")
    m = mean(values)
    return sum((x - m) ** 2 for x in values) / len(values)
