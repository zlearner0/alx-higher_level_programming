#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    '''adding 2 tuples elements'''
    if tuple_a == ():
        return tuple_b
    elif tuple_b == ():
        return tuple_a
    x = tuple_a[0] + tuple_b[0]
    if len(tuple_a) == 1 and len(tuple_b) > 1:
        y = tuple_b[1]
    if len(tuple_b) == 1 and len(tuple_a) > 1:
        y = tuple_a[1]
    if len(tuple_a) > 1 and len(tuple_b) > 1:
        y = tuple_a[1] + tuple_b[1]
    return x, y
