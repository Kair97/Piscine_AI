def find_duplicates(items):
    seen = set()
    duplicates = []
    for item in items:
        if item in seen:           # O(n) search — intentionally slow
            duplicates.append(item)
        else:
            seen.add(item)
    return duplicates

data = list(range(5000)) + list(range(2500))
print(find_duplicates(data))