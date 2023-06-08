#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    res = 0
    for index, arg in enumerate(argv):
        if index == 0:
            continue
        if arg[0] == '-':
            if arg[1:].isdigit():
                res += int(arg)
                continue
        if arg.isdigit():
            res += int(arg)
    print(f"{res:d}")
