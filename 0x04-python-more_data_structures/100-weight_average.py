#!/usr/bin/python3


def weight_average(my_list=[]):
    '''return weighted average for tuples list'''
    if (not my_list):
        return 0
    sum = 0
    div = 0
    for i, j in my_list:
        sum += i * j
        div += j
    return float(sum) / div
