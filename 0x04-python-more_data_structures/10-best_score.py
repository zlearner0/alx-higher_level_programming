#!/usr/bin/python3


def best_score(a_dictionary):
    '''give max value of a dictionary'''
    if (not a_dictionary.values()):
        return None
    if (not a_dictionary):
        return None
    return max(a_dictionary.values())
