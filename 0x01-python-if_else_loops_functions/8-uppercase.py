#!/usr/bin/python3
def uppercase(str):
    for index, letter in enumerate(str):
        letter = ord(letter)
        if letter >= 97 and letter <= 122:
            letter = letter - 32
        print("{}".format(chr(letter)), end='')
    print('\n')
