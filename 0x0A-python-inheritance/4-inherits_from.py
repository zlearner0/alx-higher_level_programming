#!/usr/bin/python3
'''this is documentation for that module
    for a function compars object with class
'''


def inherits_from(obj, a_class):
    """
    Check if obj is an instance of a class (directly or indirectly) from a_class.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
