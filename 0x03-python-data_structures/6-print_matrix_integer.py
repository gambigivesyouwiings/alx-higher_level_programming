#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for item in matrix:
        for n in item:
            print("{:d}".format(n), end=" ")
        print()
