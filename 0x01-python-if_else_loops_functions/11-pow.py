#!/usr/bin/python3
def pow(a, b):
    negative = False
    res = 1
    if b == 0:
        return 1
    elif b < 0:
        negative = True
        b = abs(b)
    for i in range(0, b):
        res *= a
    if negative:
        return 1 / res
    return res
