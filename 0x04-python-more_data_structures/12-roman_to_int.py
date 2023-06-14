#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numerical_value = 0
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    for index, ch in enumerate(roman_string):
        for key, value in roman_d.items():
            if ch == key:
                if index == 0 and len(roman_string) == 2:
                    if ch == 'I' or ch == 'X' or ch == 'C':
                        numerical_value = -value
                        continue
                numerical_value = numerical_value + value
    return numerical_value
