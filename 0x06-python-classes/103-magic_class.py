#!/usr/bin/python3

"""
This is the documentation for the module 103-magic_class.py.
"""
import math


class MagicClass:
    '''
    this is class documentation for class MagicClass
    the class gives a cricule object
'''

    def __init__(self, radius=0):
        '''
        Initializes a new circle object.
        Parameters:
        - radius: the radius of the circle (default 0)
        '''
        self.__radius = 0
        if type(radius) not in [int, float]:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Computes the area of the circle.

        Returns:
        - the area of the circle
        """
        return self.__radius**2 * math.pi

    def circumference(self):
        """
        Computes the circumference of the circle.

        Returns:
        - the circumference of the circle
        """
        return 2 * math.pi * self.__radius
