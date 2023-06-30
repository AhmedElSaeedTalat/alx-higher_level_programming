#!/usr/bin/python3
def text_indentation(text):
    new_line = 0	
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        if new_line == 1:
            print()
            print()
            new_line = 0
        if i == '.' or i == '?' or i == ':':
            new_line = 1
        print(i, end='')
    print()
