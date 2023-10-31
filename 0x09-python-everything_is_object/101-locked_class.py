#!/usr/bin/python3
''' the module give protection for attribute'''


class LockedClass:
    '''creates only protected instance attributes'''
    __slots__ = ['first_name']
