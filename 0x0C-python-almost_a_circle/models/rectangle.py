#!/usr/bin/python3
""" class Rectangle creation """
from models.base import Base


class Rectangle(Base):
    """ create class Rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            __init__(self, width, height, x=0, y=0, id=None):
            instantiate class
            Args:
                 width: width of Rectangle
                 height: height of Rectangle
        """
        super().__init__(id)
        if not type(width) == int:
            raise TypeError("width must be an integer")

        elif not type(height) == int:
            raise TypeError("height must be an integer")

        elif not type(x) == int:
            raise TypeError("x must be an integer")

        elif not type(y) == int:
            raise TypeError("y must be an integer")

        elif width <= 0:
            raise ValueError("width must be > 0")

        elif height <= 0:
            raise ValueError("height must be > 0")

        elif x < 0:
            raise ValueError("x must be >= 0")

        elif y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ width(self): getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ width(self, value): setter for width"""
        if not type(value) == int:
            raise TypeError("width must be an integer")

        elif value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """ height(self): getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ height(self, value): setter for height"""
        if not type(value) == int:
            raise TypeError("height must be an integer")

        elif value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """ x(self): getter for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ x(self, value): setter for x"""
        if not type(value) == int:
            raise TypeError("x must be an integer")

        elif value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """ y(self): getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ y(self, value): setter for y"""
        if not type(value) == int:
            raise TypeError("y must be an integer")

        elif value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """ area(self): calculates area """
        return self.__width * self.__height

    def display(self):
        """ display(self): display rectangle"""

        h = self.__height
        w = self.__width
        x = self.__x
        y = self.__y

        for i in range(y):
            print()

        for i in range(h):
            for space in range(x):
                print(' ', end='')
            for y in range(w):
                print('#', end='')
            print()

    def __str__(self):
        """ __str__(self): instance string representation"""
        class_name = self.__class__.__name__
        w = self.__width
        h = self.__height
        return f"[{class_name}] ({self.id}) {self.__x}/{self.__y} - {w}/{h}"

    def update(self, *args, **kwargs):
        """update(self, *args): assign args to each attribute"""
        args_len = len(args)
        if args_len > 0:
            i = 0
            for key in vars(self):
                setattr(self, key, args[i])
                i += 1
                if i == args_len:
                    break
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """to_dictionary(self): dict to rectangle"""
        dict1 = {}
        for key, value in vars(self).items():
            key = key.replace('_Rectangle__', '')
            dict1[key] = value
        return dict1
