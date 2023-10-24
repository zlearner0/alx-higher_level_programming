#!/usr/bin/python3

"""
This is the documentation for the module 101-magic_class.py.
"""


class Square:
    """
    This class defines a square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square object.

        Args:
            size (int): The size of the square.
            position (tuple): of 2 integers.
        """
        self.size = size
        self.position = position

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
            value (int): The size of the square.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is < 0.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """
        Gets the position of the square.

        Returns:
            The position of the square as a tuple of 2 integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): The position of the square as a tuple of 2 integers.

        Raises:
            TypeError: if value is not a tuple of 2 integers.
            ValueError: if value contains negative integers.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')

        if not isinstance(value[0], int):
            raise TypeError('position must be a tuple of 2 positive integers')

        if not isinstance(value[1], int) or value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square to stdout with the '#'
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(' ' * self.__position[0], end='')
            print('#' * self.__size)

    def __str__(self):
        """
        Returns a string representation of the square object.
        """
        s = ''
        if self.__size == 0:
            return s
        for _ in range(self.__position[1]):
            s += '\n'
        for _ in range(self.__size):
            s += ' ' * self.__position[0]
            s += '#' * self.__size
            s += '\n'
        return s[:-1]
