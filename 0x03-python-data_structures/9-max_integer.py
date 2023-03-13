#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    j = 0
    maxim = my_list[0]
    while j < len(my_list):
        if my_list[j] > maxim:
            maxim = my_list[j]
        j += 1
    return maxim
