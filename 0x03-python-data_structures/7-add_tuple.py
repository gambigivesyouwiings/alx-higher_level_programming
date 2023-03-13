#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuple_a = (0, 0)
        else:
            tuple_a += (0, )
    if len(tuple_a) > 2:
        tuple_a = tuple_a[0:2]
    if len(tuple_b) < 2:
        if len(tuple_a) == 0:
            tuple_a = (0, 0)
        else:
            tuple_b += (0, )
    if len(tuple_b) > 2:
        tuple_b = tuple_b[0:2]

    first, second = tuple_a
    moja, pili = tuple_b
    a = first + moja
    b = second + pili

    return (a, b)
