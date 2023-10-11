#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    '''multiply dictionary value by 2'''
    if (not a_dictionary):
        return None
    dict = {}
    for key, item in a_dictionary.items():
        dict[key] = 2 * item
    return dict
