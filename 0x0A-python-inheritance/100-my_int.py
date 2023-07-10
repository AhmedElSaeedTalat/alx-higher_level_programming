#!/usr/bin/python3
""" class MyInt that inherits from int """


class MyInt(int):
    """ class MyInt inherits from int """
    def __eq__(self, other):
        """ __eq__(self, other): to revert behavior """
        return not super().__eq__(other)

    def __ne__(self, other):
        """ __ne__(self, other): to revert behavior """
        return super().__eq__(other)
