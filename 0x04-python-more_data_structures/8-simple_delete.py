#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    '''remove an element from a dictionary'''
    if (not a_dictionary):
        return None
    if (a_dictionary.get(key, 0) == 0):
        return a_dictionary
    del a_dictionary[key]
    return a_dictionary
