#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5
    print("10 + 5 = {}".format(add(a, b)))
    print("10 - 5 = {}".format(sub(a, b)))
    print("10 * 5 = {}".format(mul(a, b)))
    print("10 / 5 = {}".format(div(a, b)))
