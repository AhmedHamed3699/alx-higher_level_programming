#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        start = True
        for elem in row:
            if not start:
                print(' ', end='')
            print("{:d}".format(elem), end='')
            start = False
        print('\n', end='')
