#!/usr/bin/python3
"""
This is the documentation for the module 102-square.py.
"""


class Square:
    """
    This class defines a square.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square object.

        Args:
            size (int/float): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int/float): The size of the square.

        Raises:
            TypeError: if value is not a number (int/float).
            ValueError: if value is < 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError('size must be a number')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Checks whether this square is equal to another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            True if both squares have the same area. False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Checks whether this square is not equal to another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            True if both squares don't have the same area. False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Checks whether this square is less than another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            True if square has smaller area than the other square
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Checks whether this square is less than or equal to another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            True if square has smaller area than the other square
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Checks whether square is greater than another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            True square has greater area than the other square
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Checks whether this square is greater than or equal to another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            True if square has greater area than the other square
        """
        return self.area() >= other.area()
