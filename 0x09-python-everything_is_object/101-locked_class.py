#!/usr/bin/python3
""" class with loced attribute """


class LockedClass:
    """class to lock attribute"""

    def __setattr__(self, attribute, value):
        """ __setattr__(self, attribute, value): to set attributes"""
        if attribute != "first_name":
            error = "'LockedClass' object has no attribute"
            raise AttributeError(f"{error} '{attribute}'")
        else:
            super().__setattr__(attribute, value)
