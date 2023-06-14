#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for k, val in a_dictionary.items():
        if k == key:
            a_dictionary.update({k: value})
            return a_dictionary
    a_dictionary.update({key: value})
    return a_dictionary
