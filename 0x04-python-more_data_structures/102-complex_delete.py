#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    '''delete element by value'''
    if (a_dictionary is None):
        return None
    keys_list = []
    for key, item in a_dictionary.items():
        if (item == value):
            keys_list.append(key)

    for key in keys_list:
        del a_dictionary[key]
    return a_dictionary
