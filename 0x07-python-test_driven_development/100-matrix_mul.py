#!/usr/bin/python3
"""A module for adding numbers."""


def matrix_mul(m_a=[], m_b=[]):
    """Multiply two matrices."""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if len(m_a) != 0 and not isinstance(m_a[0], list):
        raise TypeError("m_a must be a list of lists")
    if len(m_b) != 0 and not isinstance(m_b[0], list):
        raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for e in row:
            if not isinstance(e, int) and not isinstance(e, float):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for e in row:
            if not isinstance(e, int) and not isinstance(e, float):
                raise TypeError("m_b should contain only integers or floats")
    a_size = len(m_a[0])
    b_size = len(m_b[0])
    for row in m_a:
        if len(row) != a_size:
            raise TypeError("each row of m_a must be of the same size")
    for row in m_b:
        if len(row) != b_size:
            raise TypeError("each row of m_b must be of the same size")
    if a_size != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    result_matrix = []
    for i in range(len(m_a)):
        row = []
        for j in range(b_size):
            elm = 0
            for k in range(a_size):
                elm += m_a[i][k] * m_b[k][j]
            row.append(elm)
        result_matrix.append(row)
    return result_matrix
