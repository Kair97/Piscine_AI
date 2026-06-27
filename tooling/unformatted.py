def calculate(x, y, z):
    result = x * y + z
    if result > 100:
        return "high"
    elif result > 50:
        return "medium"
    else:
        return "low"


data = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}
