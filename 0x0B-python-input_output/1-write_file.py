#!/usr/bin/python3
""" writes a string to a text file & returns the number of characters"""


def write_file(filename="", text=""):
    """ write in a file and returns number of characters """
    number = 0
    with open(filename, "w", encoding="utf8") as f:
        number = f.write(text)
    return number
