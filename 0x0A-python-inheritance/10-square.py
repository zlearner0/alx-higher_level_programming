#!/usr/bin/python3
'''this is documentation for module contains class BaseGeometry has methods
'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''contains square properties and methods'''

    def __init__(self, size):
        '''inistantiate the square object'''
        self.integer_validator('width', size)
        self.__size = size

    def area(self):
        '''update the area for the square'''
        return self.__size**2

    def __str__(self):
        '''string representation for the square'''
        s = f'[Rectangle] {self.__size}/{self.__size}'
        return s
