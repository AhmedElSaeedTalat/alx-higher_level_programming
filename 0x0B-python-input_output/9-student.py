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

    def to_json(self):
        """
            to_json(self): retrieves a dictionary representation of instance
        """
        return vars(self)
