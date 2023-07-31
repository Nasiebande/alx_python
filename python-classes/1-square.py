class Square:
    """
    Represents a square with a private size attribute.
    """

    def __init__(self, size=0):
        """
        Initializes the Square instance with the given size.

        Parameters:
            size (int, optional): The size of the square (default is 0).
        """
        self.__size = 0
        self.size = size

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Parameters:
            value (int): The new size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value


# Test cases
if __name__ == "__main__":
    mysquare = Square(3)
    print(type(mysquare))
    print(mysquare.__dict__)

    mysquare = Square(89)
    print(type(mysquare))
    print(mysquare.__dict__)

    mysquare = Square()
    print(type(mysquare))
    print(mysquare.__dict__)

    try:
        mysquare = Square("3")
        print(type(mysquare))
        print(mysquare.__dict__)
    except Exception as e:
        print(e)

    try:
        mysquare = Square(3.14)
        print(type(mysquare))
        print(mysquare.__dict__)
    except Exception as e:
        print(e)

    try:
        mysquare = Square(-89)
        print(type(mysquare))
        print(mysquare.__dict__)
    except Exception as e:
        print(e)

