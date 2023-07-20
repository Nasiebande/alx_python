def fibonacci_sequence(n):
    if n <= 0:
        return []

    fibonacci = [0, 1]
    for i in range(2, n):
        next_fib = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_fib)

    return fibonacci[:n]
