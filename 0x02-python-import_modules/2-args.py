#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    length = len(argv)
    if length == 1:
        print("0 arguments.")
    elif length == 2:
        print("1 argument:")
    else:
        print(f"{length - 1} arguments:")
    for index, arg in enumerate(argv):
        if index == 0:
            continue
        print(f"{index}: {arg}")
