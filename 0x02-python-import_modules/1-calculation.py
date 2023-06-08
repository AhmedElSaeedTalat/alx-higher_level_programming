#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5
    print("10 + 5 = {}".format(add(10, 5)))
    print("10 - 5 = {}".format(sub(10, 5)))
    print("10 * 5 = {}".format(mul(10, 5)))
    print("10 / 5 = {}".format(div(10, 5)))
