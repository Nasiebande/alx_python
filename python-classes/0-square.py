#!/usr/bin/python3

class Square:
    """
    This class defines a square.

    Attributes:
        __size (int): The size of the square (private attribute).
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

# Test cases
if __name__ == "__main__":
    my_square = Square(3)
    print(type(my_square))  # Output: <class '__main__.Square'>
    print(my_square.__dict__)  # Output: {'_Square__size': 3}

    try:
        print(my_square.size)
    except Exception as e:
        print(e)  # Output: 'Square' object has no attribute 'size'

    try:
        print(my_square._Square__size)
    except Exception as e:
        print(e)  # Output: 3
