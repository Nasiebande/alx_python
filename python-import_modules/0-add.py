#!/usr/bin/python3

# Define variables a and b
a = 1
b = 2

# Define the add function
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return a + b

if __name__ == "__main__":
    # Calculate the result of add(a, b)
    result = add(a, b)

    # Print the result using string format
    print(f"{a} + {b} = {result}")
    
