#!/usr/bin/python3

from calculator_1 import add, sub


def magic_calculation(a, b):
    '''calculate sub and add'''
    if a < b:
        c = add(a, b)
        for i in range(4, 7):
            c = add(c, i)
    else:
        c = sub(a, b)
    return c
