#!/usr/bin/python3
''' This is a documentation of the module including code for test
    it runs function matrix_mul
'''


def matrix_mul(m_a, m_b):
    '''multiply 2 lists of lists of integers'''
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if m_a == []:
        raise ValueError("m_a can't be empty")
    if m_b == []:
        raise ValueError("m_b can't be empty")

    for li in m_a:
        if not isinstance(li, list):
            raise TypeError("m_a must be a list of lists")

        if li == []:
            raise ValueError("m_a can't be empty")

        if len(m_a[0]) != len(li):
            raise TypeError("each row of m_a must be of the same size")

        for item in li:
            if not isinstance(item, (int, float)):
                raise ValueError("m_a should contain only integers or floats")

    for li in m_b:
        if not isinstance(li, list):
            raise TypeError("m_b must be a list of lists")

        if li == []:
            raise ValueError("m_b can't be empty")

        if len(m_b[0]) != len(li):
            raise TypeError("each row of m_b must be of the same size")

        for item in li:
            if not isinstance(item, (int, float)):
                raise ValueError("m_b should contain only integers or floats")

    if len(m_a[0]) != len(m_b):
        raise TypeError("m_a and m_b can't be multiplied")

    result_list = []

    for i in range(len(m_a)):
        li = []
        m = 0
        for j in range(len(m_b[0])):
            n = 0
            for x in range(len(m_b[0])):
                n += m_a[i][x] * m_b[x][j]
            li.append(n)
        result_list.append(li)

    return result_list
