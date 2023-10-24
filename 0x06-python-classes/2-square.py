#!/usr/bin/python3
"""
This is the documentation for the module 4-square.py.
"""


class Square:
    """
    This is the documentation for the Square class.
    It represents a square shape with a given size.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square object.

        Parameters:
        - size (int): the size of the square (default 0)
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
