#!/usr/bin/python3
'''this is documentation for module contains class BaseGeometry with methods
'''


class BaseGeometry:
    '''this is class for a regular method area'''

    def area(self):
        '''method that raises Exception message'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''method to compare the name of class with  value of its object'''
        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
