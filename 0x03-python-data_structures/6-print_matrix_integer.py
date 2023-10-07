#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    '''print list elements separately'''
    if matrix is None:
        print("")
    else:
        for small_list in matrix:
            for i in small_list:
                print("{} ".format(i), end="" if small_list.index(
                    i) < len(small_list) - 1 else "\n")
