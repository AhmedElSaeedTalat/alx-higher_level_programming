#!/usr/bin/python3
""" create class Base """
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string(list_dictionaries): return json representation"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        return json.dumps(list_dictionaries)
