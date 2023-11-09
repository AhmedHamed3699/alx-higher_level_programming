#!/usr/bin/python3
"""A module for pascal triangle."""


def pascal_triangle(n):
    """Return a list of lists of integers for Pascal’s triangle."""
    triangle = []
    if n <= 0:
        return triangle
    triangle.append([1])
    for i in range(1, n):
        line = []
        line.append(1)
        if i > 1:
            for j in range(1, i):
                line.append(triangle[i-1][j-1] + triangle[i-1][j])
        line.append(1)
        triangle.append(line)
    return triangle
