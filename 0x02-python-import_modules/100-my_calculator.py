#!/usr/bin/python3
from sys import exit, argv
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    sign = argv[2]
    if sign == '+' or sign == '-' or sign == '*' or sign == '/':
        if sign == '+':
            print("{} {} {} = {}".format(a, sign, b, add(a, b)))
        elif sign == '-':
            print("{} {} {} = {}".format(a, sign, b, sub(a, b)))
        elif sign == '*':
            print("{} {} {} = {}".format(a, sign, b, mul(a, b)))
        else:
            print("{} {} {} = {}".format(a, sign, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
