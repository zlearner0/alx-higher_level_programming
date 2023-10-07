#!/usr/bin/python3
def no_c(my_string):
    '''remove c, C from a string'''
    updated_string = ""
    for letter in my_string:
        if letter == "c" or letter == "C":
            continue
        else:
            updated_string += letter
    return updated_string
