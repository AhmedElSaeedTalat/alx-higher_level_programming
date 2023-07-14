#!/usr/bin/python3
""" class Square inherits from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square """
    def __init__(self, size, x=0, y=0, id=None):
        """
           __init__(self, size, x=0, y=0, id=None): instantiation
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """__str__(self): string representation"""
        class_name = self.__class__.__name__
        w = super().width
        return f"[{class_name}] ({self.id}) {super().x}/{super().y} - {w}"
