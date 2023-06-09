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

    @property
    def size(self):
        """ size(self): return size """
        return self.width

    @size.setter
    def size(self, value):
        """ sets size value """
        self.width = value
        self.height = value

    def __str__(self):
        """__str__(self): string representation"""
        class_name = self.__class__.__name__
        w = super().width
        return f"[{class_name}] ({self.id}) {super().x}/{super().y} - {w}"

    def update(self, *args, **kwargs):
        """ update(self, *args, **kwargs): assigns arguments"""
        args_len = len(args)
        if args_len > 0:
            i = 0
            for key in vars(self):
                if key == "_Rectangle__height":
                    setattr(self, key, self.width)
                    continue
                setattr(self, key, args[i])
                i += 1
                if i == args_len:
                    break
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ to_dictionary(self):class to dictionary"""
        dict1 = {}
        for key, value in vars(self).items():
            key = key.replace('_Rectangle__', '')
            if key == "width":
                key = "size"
            if key == "height":
                continue
            dict1[key] = value
        return dict1
