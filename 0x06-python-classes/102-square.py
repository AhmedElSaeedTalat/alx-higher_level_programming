#!/usr/bin/python3
""" class Square that defines a square """


class Square:
    """
        class Square that defines a square
        Attributes:
            __size (int): private size of square
        Methods:
            __init__(self, size=0): initializes instance of the class
    """
    def __init__(self, size=0):
        """
            __init__(self, size=0): initializes instance of the class
            Args:
               size (int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
            area(self): returns the current square area
        """
        return self.__size * self.__size

    def __it__(self, other):
        return self.area() < other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __le__(self, other):
        return self.__it__(other) or self.__eq__(other)

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    @property
    def size(self):
        """
            size(self): retrieves the size
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
            size(self): sets the size
            Args:
                size (int): size passed
        """
        if not isinstance(size, (int, float)):
            raise TypeError("size must be a number")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
