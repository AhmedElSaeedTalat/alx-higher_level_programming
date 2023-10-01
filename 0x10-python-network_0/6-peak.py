#!/usr/bin/python3
""" find peak number """


def find_peak(list_of_integers):
    """ find_peak(list_of_integers): to find peak
        Args:
            list_of_integers: list passed
        Return: peak
    """
    if list_of_integers is None or len(list_of_integers) == 0:
        return None
    lst = list_of_integers
    for i in range(0, len(lst)):
        if i == 0:
            if lst[i] > lst[i + 1]:
                peak = lst[i]
                return peak
        elif i != 0 and i != len(lst) - 1:
            j = i - 1
            y = i + 1
            if lst[i] > lst[j] and lst[i] > lst[y]:
                peak = lst[i]
                return peak
        elif i == len(lst) - 1:
            if lst[i] > lst[i - 1]:
                peak = lst[i]
                return peak
    return lst[0]
