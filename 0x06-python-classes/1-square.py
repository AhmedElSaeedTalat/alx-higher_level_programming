#!/usr/bin/python3
""" a class Square that defines a square """


class Square:
    """
        this class defines a square
        Attributes:
            __size (int): private attribute for size of square
        Methods:
            __init__(self, size): initializes new instance of square with size
    """
    def __init__(self, size):
        """
            __init__(self, size): initializes new instance of square with size
            Args:
                size (int): size is the size provided for the square
        """
        self.__size = size
