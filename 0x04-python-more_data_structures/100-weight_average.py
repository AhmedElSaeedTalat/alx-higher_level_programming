#!/usr/bin/python3
def weight_average(my_list=[]):
    res = 1
    div = 0
    avg = 0
    if not my_list:
        return 0
    for ind, i in enumerate(my_list):
        if ind > 0:
            avg = avg + res
            res = 1
        for index, y in enumerate(i):
            res = res * y
            if index > 0:
                div = div + y
    avg = avg + res
    return avg / div
