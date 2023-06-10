#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for index, y in enumerate(i):
            if index == len(i) - 1:
                print("{}".format(y), end='')
                continue
            print("{} ".format(y), end='')
        print()
