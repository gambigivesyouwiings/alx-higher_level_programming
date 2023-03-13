#!/usr/bin/python3
def no_c(my_string):
    list = [i for a, i in enumerate(my_string)]
    for char in list:
        if char in "cC":
            list.remove(char)

        new = "".join(list)
        return new
