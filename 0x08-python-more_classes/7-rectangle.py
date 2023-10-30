#!/usr/bin/python3
'''this is documentation for the created module
'''


class Rectangle:
    ''' this is empty class Rectangle'''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''setting width and height of a rectangle'''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        '''method calculate the rectangle area'''
        return self.__width * self.__height

    def perimeter(self):
        '''method to calculate rectangle perimeter'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * self.__width + 2 * self.__height

    def __str__(self):
        ''' returns string representation for the object'''
        if self.__width == 0 or self.__height == 0:
            return ""
        txt = ""
        for h in range(self.__height):
            txt += str(self.print_symbol) * self.__width + "\n"
        return txt[:-1]

    def __repr__(self):
        ''' returns string representation for the object code'''
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        ''' method to print message when deleting an object '''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
