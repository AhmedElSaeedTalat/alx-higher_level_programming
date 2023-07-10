#!/usr/bin/python3
""" function  returns True if the object is an instance of parent only"""


def inherits_from(obj, a_class):
    """
        def inherits_from(obj, a_class): return true if obj is
        instance of parent classes only
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
