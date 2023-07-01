#!/usr/bin/python3
""" function to print first and last name passed """


def say_my_name(first_name, last_name=""):
    """
        def say_my_name(first_name, last_name=""): function to print name
        Args:
            first_name: first name passed
            last_name: last name passed with default value
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if not first_name:
        return None
    if isinstance(first_name, str):
        if first_name.isspace():
            return None
    print("My name is {} {}".format(first_name, last_name))
