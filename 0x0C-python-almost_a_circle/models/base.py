#!/usr/bin/python3
""" create class Base """
import json
import os


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
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save_to_file(cls, list_objs): to save json to file"""
        if list_objs is None:
            list_objs = []
        dicts = []
        for obj in list_objs:
            dicts.append(obj.to_dictionary())
        json_string = cls.to_json_string(dicts)
        with open(cls.__name__ + ".json", "w") as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """ from_json_string(json_string): convert from json"""
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create(cls, **dictionary): create instance and update attr"""
        if cls.__name__ == "Rectangle":
            new_instance = cls(5, 5)
            new_instance.update(**dictionary)
        if cls.__name__ == "Square":
            new_instance = cls(5)
            new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """ load_from_file(cls):returns a list of instances"""
        if not os.path.exists(cls.__name__ + ".json"):
            return []
        list_instances = []
        with open(cls.__name__ + ".json") as f:
            obj_dicts = cls.from_json_string(f.read())
        for dict1 in obj_dicts:
            list_instances.append(cls.create(**dict1))
        return list_instances
