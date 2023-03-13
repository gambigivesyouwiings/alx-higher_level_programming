#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for item in matrix:
        for n in item:
            if n == item[-1]:
                print('{:d}'.format(n), end='')
            else:
                print('{:d}'.format(n), end=' ')
        print()
