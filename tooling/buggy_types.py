def add(a: int, b: int) -> int:
    return a + b

result: int = add(1, 2)        # Error: int assigned to str
items: list[int] = [1, 2, 3]  # Error: str in list[int]

def greet(name: str) -> str:
    return "42"                  # Error: return int from str function