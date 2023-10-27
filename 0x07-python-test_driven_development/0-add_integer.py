#!/usr/bin/python3
''' This is a documentation of the module including code for test
    it contains function add_integer that adds two numbers
'''


def add_integer(a, b=98):
    '''
    Add two numbers
    Args:
    - a: a float or integer number
    - b: a float or integer number
    Raises:
    - TypeError if input is not integer or float
    Return:
    - the sum of both numbers
    '''
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
