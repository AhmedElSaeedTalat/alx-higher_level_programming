#!/usr/bin/python3
def uppercase(str):
    for index, letter in enumerate(str):
        letter = ord(letter)
        if letter >= 97 and letter <= 122:
            letter = letter - 32
        if index == len(str) - 1:
            print("{}".format(chr(letter)),end='\n')
            continue
        print("{}".format(chr(letter)), end='')
