#!/usr/bin/python3
for i in range(0, 10):
    for y in range(i + 1, 10):
        if y == 9 and i == 8:
            print(f"{i}{y}")
            continue
        print(f"{i}{y}, ", end='')
