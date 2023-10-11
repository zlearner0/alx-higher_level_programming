#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    '''delete element by value'''
    if (not a_dictionary):
        return None
    keys_list = []
    for key, item in a_dictionary.items():
        if (item == value):
            keys_list.append(key)

    for key in keys_list:
        del a_dictionary[key]
