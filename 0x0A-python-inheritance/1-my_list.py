#!/usr/bin/python3
""" class MyList that inherits from list """


class MyList(list):
    """ class inherits from list """

    def __init__(self):
        """ __init__(self): to initialize instance """
        super().__init__()

    def print_sorted(self):
        """
            def print_sorted(self):  prints list sorted
        """
        print(sorted(self))
