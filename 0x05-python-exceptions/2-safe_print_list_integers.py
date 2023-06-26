#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    counter = 0
    try:
        while (i < x):
            if not isinstance(my_list[i], int):
                i = i + 1
                continue
            print("{:d}".format(my_list[i]), end='')
            i = i + 1
            counter = counter + 1
    except (ValueError, TypeError):
        pass
    print()
    return counter
