#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    b = my_list[::-1]
    if my_list:
        for item in b:
            print("{:d}".format(item))
    my_list = b
