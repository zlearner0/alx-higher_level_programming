#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    '''print list elements in reverse order'''
    my_list.reverse()
    for item in my_list:
        print("{}".format(item))
