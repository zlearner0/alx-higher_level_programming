#!/usr/bin/python3


def best_score(a_dictionary):
    '''give max value of a dictionary'''
    if (max(a_dictionary.values()) is None):
        return None
    return max(a_dictionary.values())
