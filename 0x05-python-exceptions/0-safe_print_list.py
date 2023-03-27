#!/bin/python3
def safe_print_list(my_list=[], x=0):
    listed = []
    if x == 0:
        listed.append(my_list[0])

    for item in range(0, x):
        try:
            listed.append(my_list[item])
        except IndexError:
            break
    return listed
