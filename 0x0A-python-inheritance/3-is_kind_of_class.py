#!/usr/bin/python3
""" function  returns True if the object is an instance of cls """


def is_kind_of_class(obj, a_class):
    """
        def is_kind_of_class(obj, a_class): return true if obj is
        instance of cls
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
