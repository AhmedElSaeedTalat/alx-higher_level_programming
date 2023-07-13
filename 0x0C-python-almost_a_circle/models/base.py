#!/usr/bin/python3
""" create class Base """


class Base:
    """ class base created """

    __nb_objects = 0

    def __init__(self, id=None):
        """ __init__(self, id=None): instantiate class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
