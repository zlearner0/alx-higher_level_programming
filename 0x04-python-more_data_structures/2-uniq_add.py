#!/usr/bin/python3
def uniq_add(my_list=[]):
    '''returns a unique elements list'''
    if (not my_list):
        return None
    my_set = set(my_list)
    return sum(my_set)
