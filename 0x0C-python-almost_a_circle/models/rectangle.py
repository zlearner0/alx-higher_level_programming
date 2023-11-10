#!/usr/bin/python3
'''this module contains class Rectangle'''

# from base import Base
# Base = __import__('base').Base

from models.base import Base


class Rectangle(Base):
    '''reprsents a rectangle shape'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''initializing object for the class'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''width getter'''
        return self.__width

    @width.setter
    def width(self, value):
        '''width setter'''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 1:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        '''height getter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''height setter'''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 1:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        '''x getter'''
        return self.__x

    @x.setter
    def x(self, value):
        '''x setter'''
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        '''y getter'''
        return self.__y

    @y.setter
    def y(self, value):
        '''y setter'''
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        '''calculate the area of the shape'''
        return self.__width * self.__height

    def display(self):
        '''visual display for the shape'''
        for j in range(self.__y):
            print(' ')
        for i in range(self.__height):
            print(self.__x * ' ' + self.__width * '#')

    def __str__(self):
        '''string representation for rectangle class'''
        clsnm = type(self).__name__
        id = self.id
        x = self.__x
        y = self.__y
        width = self.__width
        height = self.__height
        if clsnm == 'Rectangle':
            return '[{}] ({}) {}/{} - {}/{}'.format(clsnm, id, x, y, width,
                                                    height)
        if clsnm == 'Square':
            return '[{}] ({}) {}/{} - {}'.format(clsnm, id, x, y, width)

    def update(self, *args, **kwargs):
        '''updates the attributes of the object'''
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]

        if args is None or args == ():
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''dictionary representation for the object'''
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
