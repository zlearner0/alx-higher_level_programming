#!/usr/bin/python3


def remove_char_at(str, n):
    '''removes a character in a string'''
    new_str = ""
    for i, c in enumerate(str):
        if i != n:
            new_str = new_str + c
    return new_str
