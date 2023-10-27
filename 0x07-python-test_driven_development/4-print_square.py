#!/usr/bin/python3
''' This is a documentation of the module including code for test
    it contains function draws square
'''


def print_square(size):
    '''
    prints a square using #
    Args:
        size: integer for the length of a square
    Raises:
        TypeError: if not integer
        ValueError: if value less than 0
    Return:
        nothing
    '''
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
