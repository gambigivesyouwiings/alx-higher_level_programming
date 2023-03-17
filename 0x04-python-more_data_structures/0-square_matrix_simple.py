#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = []
    for row in matrix:
        b = list(map(lambda x: x*x, row))
        square.append(b)
    return square

matrix = [[3,2,1],[5,6,7]]
print(square_matrix_simple(matrix))
