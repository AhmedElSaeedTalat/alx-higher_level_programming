#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numerical_value = 0
    temp = 0
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    for index, ch in enumerate(roman_string):
        value = roman_d.get(ch)
        if value > temp and index > 0:
            numerical_value = value - numerical_value
        else:
            numerical_value = numerical_value + value
        temp = value
    return numerical_value
