#!usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''return the square of elements of original list'''
    if (not matrix):
        return None
    sqr_mtx = []
    for small_mtrx in matrix:
        sqr = []
        for item in small_mtrx:
            sqr.append(item**2)
        sqr_mtx.append(sqr)
    return sqr_mtx
