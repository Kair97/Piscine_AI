from typing import Any

VERSION: str = "1.0"


def mean(values: list[float]) -> float:
    """Computes the arithmetic mean of a list of floats."""
    if not values:
        raise ZeroDivisionError("Cannot compute mean of an empty list.")
    return sum(values) / len(values)


def median(values: list[float]) -> float:
    """Computes the median of a list of floats."""
    if not values:
        raise ValueError("Cannot compute median of an empty list.")
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    mid = n // 2
    if n % 2 == 1:
        return sorted_vals[mid]
    else:
        return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2.0


def variance(values: list[float]) -> float:
    """Computes the variance of a list of floats."""
    if not values:
        raise ValueError("Cannot compute variance of an empty list.")
    m = mean(values)
    return sum((x - m) ** 2 for x in values) / len(values)


def process_records(
    records: list[dict[str, Any]], key: str, default: Any = None
) -> list[Any]:
    return [r.get(key, default) for r in records]


def merge_dicts(a: dict[str, int], b: dict[str, int]) -> dict[str, int]:
    return {**a, **b}


if __name__ == "__main__":
    result = merge_dicts({"x": 1}, {"y": 2})
    print(result)
