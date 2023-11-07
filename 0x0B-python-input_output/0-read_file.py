#!/usr/bin/python3
'''this module contains function to read a file'''


def read_file(filename=""):
    '''opens a file then read and print it'''
    with open(filename, 'r') as rf:
        print(rf.read(), end='')
