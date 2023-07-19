def pow(a, b):
    result = 1
    for _ in range(b):
        result *= a
    return result
print(pow(2, 3))