#!/usr/bin/python3
""" function to add attribute to an instance """


def add_attribute(obj, name, value):
    """ add_attribute(obj, name, value): to add attribute """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
