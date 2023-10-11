#!/usr/bin/python3
def uniq_add(my_list=[]):
    if (my_list is None):
        return None
    if (my_list == []):
        return 0
    '''returns a unique elements list'''
    my_set = set(my_list)
    return sum(my_set)
