#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    bigKey, bigValue = None, -1e6
    for key, value in a_dictionary.items():
        if value > bigValue:
            bigValue = value
            bigKey = key
    return bigKey
