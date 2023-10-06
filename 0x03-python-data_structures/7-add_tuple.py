#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    first = 0 if len(tuple_a) < 1 else tuple_a[0]
    first += 0 if len(tuple_b) < 1 else tuple_b[0]
    second = 0 if len(tuple_a) < 2 else tuple_a[1]
    second += 0 if len(tuple_b) < 2 else tuple_b[1]
    return (first, second)
