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
        self.__width = width
        self.__height = height
        self.__x = x
        self.y = y

    @property
    def width(self):
        """ width(self): getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ width(self, value): setter for width"""
        self.__width = value

    @property
    def height(self):
        """ height(self): getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ height(self, value): setter for height"""
        self.__height = value

    @property
    def x(self):
        """ x(self): getter for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ x(self, value): setter for x"""
        self.__x = value

    @property
    def y(self):
        """ y(self): getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ y(self, value): setter for y"""
        self.__y = value
