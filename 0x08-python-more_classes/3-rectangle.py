#!/usr/bin/python3
""" a class that defines a rectangle """


class Rectangle:
    """ a class that defines a Rectangle """

    def __init__(self, width=0, height=0):
        """
            __init__(self, width=0, height=0: initialize
           instance of a class
           Args:
               width: width of rectangle passed
               height: height of rectangle passed
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property
    def width(self):
        """ def width(self): retrieves width """
        return self.__width

    @width.setter
    def width(self, value):
        """
            def width(self, value): sets width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ def height(self): retrieves height """
        return self.__height

    @height.setter
    def height(self, value):
        """
            def height(self, value): sets width
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
            def area(self): returns the area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
            def perimeter(self): returns the rectangle perimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """
            def area(self): returns the area
        """
        h = self.__height
        w = self.__width
        if h == 0 or w == 0:
            return ''
        rect = ''
        for i in range(h):
            if i > 0:
                rect += '\n'
            for y in range(w):
                rect += '#'
        return rect
