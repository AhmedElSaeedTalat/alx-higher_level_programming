#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix) == 0:
        return None
    new_matrix = [[None] * len(matrix) for i in range(len(matrix))]
    for index, i in enumerate(matrix):
        for index2, y in enumerate(i):
            new_matrix[index][index2] = y * y
    return new_matrix
