#!/usr/bin/python3


def magic_calculation(a, b, c):
    '''calculate three numbers'''
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return a * b - c
