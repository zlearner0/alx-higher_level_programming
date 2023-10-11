#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    '''returns a set of the different of 2 sets'''
    if (not set_1):
        return set_2
    if (not set_2):
        return
    if (not set_1 and not set_2):
        return None
    return set_1.symmetric_difference(set_2)
