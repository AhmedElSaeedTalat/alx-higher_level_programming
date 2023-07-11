#!/usr/bin/python3
""" function to read from a file """


def read_file(filename=""):
    """ read_file(filename=''): to read from a file"""
    with open(filename, "r", encoding="UTF8") as f:
        print(f.read(), end='')
