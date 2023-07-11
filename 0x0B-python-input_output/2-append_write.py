#!/usr/bin/python3
""" function that appends a string at the end of a text file """


def append_write(filename="", text=""):
    """ append_write(filename='', text=''): append str to file """
    number = 0
    with open(filename, "a", encoding="utf8") as f:
        number = f.write(text)
    return number
