#!/usr/bin/python3
Square = __import__('1-square').Square

my_square = Square(3)
print(type(my_square))             # <class '1-square.Square'>
print(my_square.__dict__)          # {'_Square__size': 3}

try:
    print(my_square.size)          # Should raise AttributeError
except Exception as e:
    print(e)

try:
    print(my_square.__size)        # Should raise AttributeError
except Exception as e:
    print(e)
