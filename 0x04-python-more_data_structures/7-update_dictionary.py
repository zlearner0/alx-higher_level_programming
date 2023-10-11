#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    '''add or update values'''
    if (not a_dictionary):
        return None
    a_dictionary[key] = value
    return a_dictionary
