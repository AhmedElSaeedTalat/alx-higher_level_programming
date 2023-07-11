#!/usr/bin/python3
""" inster text after a strting """


def append_after(filename="", search_string="", new_string=""):
    """ inster text after a strting """
    lines = []
    with open(filename, "r", encoding="utf8") as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if search_string in line:
            lines.insert(i + 1, new_string)
    with open(filename, "w", encoding="utf8") as f:
        for line in lines:
            f.write(line)
