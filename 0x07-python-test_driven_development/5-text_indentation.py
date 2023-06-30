#!/usr/bin/python3
""" function to add lines after special characters """


def text_indentation(text):
    """
        def text_indentation(text): adds lines after special chars
        Args:
            text: text passed to edit
    """
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
