#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    l1 = list(tuple_a)
    l2 = list(tuple_b)
    if len(l1) < 2:
        if len(l1) == 0:
            l1.append(0)
            l1.append(0)
        elif len(l1) == 1:
            l1.append(0)
    if len(l2) < 2:
        if len(l2) == 0:
            l2.append(0)
            l2.append(0)
        elif len(l2) == 1:
            l2.append(0)
    first = l1[0] + l2[0]
    second = l1[1] + l2[1]
    return (first, second)
