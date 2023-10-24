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
        self.__size = size
        """
        Initializes a new Square object.

        Parameters:
        - size (int): the size of the square (default 0)
        """

    def area(self):
        """
        Computes the area of the square.

        Returns:
        - the area of the square (int)
        """
        return self.__size**2

    @property  # getter
    def size(self):
        """
        Getter method for the size property.

        Returns:
        - the size of the square (int)
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size property.

        Parameters:
        - value (int): the new size value

        Raises:
        - TypeError: if the value is not an integer
        - ValueError: if the value is negative
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
