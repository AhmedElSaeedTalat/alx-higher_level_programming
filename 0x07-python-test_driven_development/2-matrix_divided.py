#!/usr/bin/python3
def matrix_divided(matrix, div):
    l1 = []
    len_first_r = len(matrix[0])
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(i, list) for i in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        if len(i) != len_first_r:
            raise TypeError("Each row of the matrix must have the same size")
        if not all(isinstance(y, (int, float)) for y in i):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    for i in matrix:
        l1.append(list(map(lambda a: round(a / div, 2), i)))
    return l1
