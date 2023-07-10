#!/usr/bin/python3
""" function that returns True if the object is exactly an instance """


def is_same_class(obj, a_class):
    """
        def is_same_class(obj, a_class): return true if obj is instance of cls
    """
    if type(obj) == a_class:
        return True
    else:
        return False
