#!/usr/bin/python3


def best_score(a_dictionary):
    '''give max value of a dictionary'''
    if (a_dictionary is None):
        return None
    for key, val in a_dictionary.items():
        if max(a_dictionary.values()) == val:
            return key
