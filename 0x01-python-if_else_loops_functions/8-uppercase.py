#!/usr/bin/python3

def uppercase(str):
    '''change to upper case'''
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
            print("{}".format(c), end="")
        else:
            print("{}".format(c), end="")
    print("")
