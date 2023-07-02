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
    if not text.strip():
        return
    text = text.replace(".", ".\n").replace("?", "?\n").replace(":", ":\n")
    text = text.splitlines()
    l1 = []
    for i in text:
        l1.append(i.strip())
    length = len(l1)
    for index, i in enumerate(l1):
        if index + 1 == length:
            print(i, end='')
            break
        idx = index + 1
        if l1[idx] == '?' or l1[idx] == ':' or l1[idx] == '.':
            print(i, end='')
        else:
            print(i)
            if i != '':
                print()
