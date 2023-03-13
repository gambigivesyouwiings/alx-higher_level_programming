#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    b = my_list[::-1]
    for item in b:
        print("{:d}".format(item))
