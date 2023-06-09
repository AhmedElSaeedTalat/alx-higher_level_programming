#!/usr/bin/python3
"""  class Student that defines a student"""


class Student:
    """class Student that defines a student """
    def __init__(self, first_name, last_name, age):
        """
            __init__(self, first_name, last_name, age): instantiate class
            Args:
                 first_name: passed first name
                 last_name: passed last name
                 age: passed age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            to_json(self, attrs=None): retrieves a dictionary
            representation of instance
        """
        new_dict = {}
        if attrs is not None:
            if len(attrs) > 0:
                for i in attrs:
                    if hasattr(self, i):
                        new_dict[i] = getattr(self, i)
        else:
            new_dict = vars(self)
        return new_dict

    def reload_from_json(self, json):
        """
            reload_from_json(self, json): replaces all attributes
            from Student Instance
        """
        for attribute in vars(self):
            for key, value in json.items():
                if key == attribute:
                    setattr(self, attribute, value)
