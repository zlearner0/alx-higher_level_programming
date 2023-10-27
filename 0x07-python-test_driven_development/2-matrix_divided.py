#!/usr/bin/python3
''' This is a documentation of the module including code for test
    it contains function matrix_divided that divids a list with a divisor
'''


def matrix_divided(matrix, div):
    '''
    the function divides all elements of a matrix
    Args:
        matrix: is matrix for many equal matrices
        div: is the divisor integer or float number
    Raise:
        TypeError: if matrices or div are not number and not equal matrices
    Return:
        matrix resulting from dividing original matrix
    '''

    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for li in matrix:
        if not isinstance(li, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if li == []:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        for item in li:
            if not isinstance(item, (int, float)):
                raise TypeError(
                 "matrix must be a matrix (list of lists) of integers/floats")
        if len(matrix[0]) != len(li):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = [[round(x / div, 2) for x in inner_list] for inner_list in matrix]

    return result
