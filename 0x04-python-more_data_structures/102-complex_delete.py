#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    found_key = []
    for key, value1 in a_dictionary.items():
        if value1 == value:
            found_key.append(key)
    if found_key:
        for i in found_key:
            del a_dictionary[i]
    return a_dictionary
