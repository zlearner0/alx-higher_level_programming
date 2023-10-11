#!/usr/bin/python3
def common_elements(set_1, set_2):
    '''returns a set of the comment elements of 2 sets'''
    if (not set_1):
        return set_2
    if (not set_2):
        return set_1
    if (not set_1 and not set_2):
        return None
    return set_1.intersection(set_2)
