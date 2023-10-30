#!/usr/bin/python3
'''this is documentation for the created module
'''


class Rectangle:
    ''' this is empty class Rectangle'''
    def __init__(self, width=0, height=0):
        '''setting width and height of a rectangle'''
        self.width = width
        self.height = height

    @property
    def width(self):
        ''' getter of instance attribute width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter of instance attribute width'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        ''' getter of instance attribute height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter of instance attribute width'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
