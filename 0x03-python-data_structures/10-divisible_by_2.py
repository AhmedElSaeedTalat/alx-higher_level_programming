#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    l2 = []
    for i in my_list:
        if i % 2 == 0:
            l2.append(True)
        else:
            l2.append(False)
    return l2
