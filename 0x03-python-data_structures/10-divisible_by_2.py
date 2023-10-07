#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    '''equivalent list with true and false'''
    bool_list = []
    for i in my_list:
        x = True if i % 2 == 0 else False
        bool_list.append(x)
    return bool_list
