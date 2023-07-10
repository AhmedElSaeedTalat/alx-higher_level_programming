#!/usr/bin/python3
""" an empty class BaseGeometry """


class BaseGeometry:
    """ an empty class BaseGeometry """
    def area(self):
        """ def area(self): raises exceptopn """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            def integer_validator(self, name, value): validates value
            Args:
                name: name
                value: value
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        else:
            self.name = name
            self.value = value
