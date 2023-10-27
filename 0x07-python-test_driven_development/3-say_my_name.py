#!/usr/bin/python3
''' This is a documentation of the module including code for test
    it contains function add_integer that adds two numbers
'''


def say_my_name(first_name, last_name=""):
    '''
    prints the full name
    Args:
        first_name: string of first name
        last_name: string of last name
    Raises:
        TypeError: when args are not string
    Return: nothing
    '''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
