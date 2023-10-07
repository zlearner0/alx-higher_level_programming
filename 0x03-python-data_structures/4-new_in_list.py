#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    '''created modified copy of a list'''
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    copied_list = my_list.copy()
    copied_list[idx] = element
    return copied_list
