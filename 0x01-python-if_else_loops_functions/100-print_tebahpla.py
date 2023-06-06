#!/usr/bin/python3
for index, i in enumerate(range(122, 96, -1)):
    if index % 2 != 0:
        i = i - 32
    print("{}".format(chr(i)), end='')
