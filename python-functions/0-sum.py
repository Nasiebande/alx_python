def add(a, b):
    # Perform addition using bitwise operations
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1

    return a

def add_with_negatives(a, b):
    if b < 0:  # If b is negative, convert it to positive using bitwise negation
        b = add(~b, 1)
    return add(a, b)
