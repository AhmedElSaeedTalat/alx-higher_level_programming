#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        return []
    new_matrix = [[None] * len(matrix) for i in range(len(matrix))]
    for index, i in enumerate(matrix):
        for index2, y in enumerate(i):
            new_matrix[index][index2] = int(y ** 2)
    return new_matrix
