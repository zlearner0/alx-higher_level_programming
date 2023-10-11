#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    '''sort and print a dictionary'''
    if (not a_dictionary):
        return None
    tmp = dict(sorted(a_dictionary.items()))
    for k, v in tmp.items():
        print("{}: {}".format(k, v))
