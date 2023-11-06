#!/usr/bin/python3
'''this is documentation for module contains add_attribute method
'''


def add_attribute(obj, attr, value):
    '''adds a new attribute to an object'''
    if hasattr(obj, attr):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
