def pow(a, b):
    result = 1

    if b < 0:
        a = 1 / a
        b = -b

    while b > 0:
        if b % 2 == 1:
            result *= a
        a *= a
        b //= 2

    # Round the result to 10 decimal places
    return round(result, 10)
