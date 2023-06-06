#!/usr/bin/python3
def uppercase(str):
    if str is None:
        print('\n')
    else:
        for index, letter in enumerate(str):
            letter = ord(letter)
            if letter >= 97 and letter <= 122:
                letter = letter - 32
            if index == len(str) - 1:
                print("{}".format(chr(letter)))
                continue
            print("{}".format(chr(letter)), end='')
