#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    roman_digits = {'I': 1, 'V': 5, 'X': 10,
                    'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number = 0
    i = 0
    while i < len(roman_string):
        elm = roman_string[i]
        if i + 1 < len(roman_string):
            next_elm = roman_string[i+1]
        else:
            next_elm = None
        if not next_elm or roman_digits[next_elm] <= roman_digits[elm]:
            number += roman_digits[elm]
        else:
            number += (roman_digits[next_elm] - roman_digits[elm])
            i += 1
        i += 1
    return number
