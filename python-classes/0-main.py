Square = __import__('0-square').Square

mysquare = Square(3)
print(type(mysquare))
print(mysquare.__dict__)

try:
    print(mysquare.size)
except Exception as e:
    print(e)

try:
    print(mysquare.__size)
except Exception as e:
    print(e)
