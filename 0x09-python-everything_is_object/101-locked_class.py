#!/usr/bin/python3


class LockedClass:
    '''creates only protected instance attributes'''
    __slots__ = ['first_name']

    def __init__(self):
        '''sets the instance attribute empty'''
        self.first_name = ''
