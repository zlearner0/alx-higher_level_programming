#!/usr/bin/python3
'''this is documentation for module contains class BaseGeometry has methods
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''child class to check rectanble width and height'''

    def __init__(self, width, height):
        '''initantiate object of rectangle and verify its dimensions'''
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        '''method to calculate the area of the rectangle'''
        return self.__width * self.__height

    def __str__(self):
        '''string representatio for the rectangle'''
        s = f'[Rectangle] {self.__width}/{self.__height}'
        return s
