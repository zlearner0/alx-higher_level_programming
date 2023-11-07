#!/usr/bin/python3
'''this module contains function to append to a file'''


def append_write(filename="", text=""):
    '''append text to existing file'''
    with open(filename, 'a') as af:
        size = af.write(text)
    return size
