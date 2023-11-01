#!/usr/bin/python3
"""A module for matrix division."""


def matrix_divided(matrix, div):
    """Divides a matrix by a number."""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix " +
                        "(list of lists) of integers/floats")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not matrix:
        return None
    if len(matrix) == 0:
        return []
    row_size = len(matrix[0])
    new_matrix = []
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix " +
                            "(list of lists) of integers/floats")
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for number in row:
            if not isinstance(number, int) and not isinstance(number, float):
                raise TypeError("matrix must be a matrix " +
                                "(list of lists) of integers/floats")
            new_row.append(round(number / div, 2))
        new_matrix.append(new_row)
    return new_matrix
