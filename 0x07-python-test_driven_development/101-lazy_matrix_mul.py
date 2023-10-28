#!/usr/bin/python3
''' This is a documentation of the module including code for test
    it contains function lazy_matrix_mul that multipy 2 matrices
'''
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    multipy 2 matrices
    Args:
        m_a: first matrix
        m_b: second matrix
    Return:
        matrices multiplication
    """
    return numpy.matmul(m_a, m_b)
