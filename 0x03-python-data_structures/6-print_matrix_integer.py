#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    '''print list elements separately'''
    if not matrix:
        return None
    for small_list in matrix:
        if len(small_list) == 0:
            print()
        for i in small_list:
            print("{:d}".format(i), end=" " if small_list.index(
                i) < len(small_list) - 1 else "\n")
