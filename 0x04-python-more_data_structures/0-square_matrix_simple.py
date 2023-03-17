#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = []
    new = matrix
    for row in new:
        b = list(map(lambda x: x*x, row))
        square.append(b)
    return square
