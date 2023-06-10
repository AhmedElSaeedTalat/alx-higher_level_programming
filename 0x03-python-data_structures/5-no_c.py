#!/usr/bin/python3
def no_c(my_string):
    for i, char in enumerate(my_string):
        if char == 'c' or char == 'C':
            my_string = my_string.translate({ord(char): None})
            continue
    return my_string
