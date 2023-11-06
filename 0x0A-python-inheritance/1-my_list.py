#!/usr/bin/python3
'''this is documentation for that module
    contains classes list and Mylist
'''


class MyList(list):
    '''contains method to print a list attribute'''

    def print_sorted(self):
        '''sort a list and print it ascendingly'''
        print(sorted(self))
