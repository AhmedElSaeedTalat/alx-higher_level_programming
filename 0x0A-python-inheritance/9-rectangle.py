#!/usr/bin/python3
""" a class Rectangle that inherits from BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ a class Rectangle that inherits from BaseGeometry """
    def __init__(self, width, height):
        """
            def __init__(self, width, height): init function
            Args:
                 width: width passed
                 height: height passed
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ area(self): calculates area """
        return self.__width * self.__height

    def __str__(self):
        """ __str__(self): return obj representation """
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
