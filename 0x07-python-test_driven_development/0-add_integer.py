#!/usr/bin/python3
""" function to add two integers """


def add_integer(a, b=98):
    """
        add_integer(a, b=98): to add a and b and raise a TypeError
        if a or b not a float or integer
        Args:
            a: integer or float a
            b: integer or float b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    result = int(a) + int(b)
    return result
