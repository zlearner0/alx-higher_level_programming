#!/usr/bin/python3
'''this module contains function to write in a file'''


def write_file(filename="", text=""):
    '''function writes a string to a file'''
    with open(filename, 'w') as wf:
        size = wf.write(text)

    return size
