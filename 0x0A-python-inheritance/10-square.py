#!/usr/bin/python3
""" class Square that inherits from Rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class that inherits from rectangle """
    def __init__(self, size):
        """ __init__(self, size): instantiation
            Args:
                 size: size of the rectangle
        """
        super().__init__(size, size)
        super().integer_validator("size", size)
        self.__size = size
