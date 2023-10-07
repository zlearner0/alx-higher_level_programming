#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    '''print list elements in reverse order'''
    if my_list == [] or my_list is None:
        return None
    my_list.reverse()
    for item in my_list:
        print("{:d}".format(item))
