def deep_merge(a: dict, b: dict) -> dict:
    for key, value in b.items():
        if key in a and isinstance(a[key], dict):
            a[key] = deep_merge(a[key], value)
        else:
            a[key] = value
    return a