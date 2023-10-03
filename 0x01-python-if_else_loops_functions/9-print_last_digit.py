#!/usr/bin/python3


def print_last_digit(number):
    '''prints last digit of a number'''
    num = number if number > -1 else -number
    num %= 10
    print("{:d}".format(num), end="")
    return num
