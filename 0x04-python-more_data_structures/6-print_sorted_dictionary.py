#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    my_dict = sorted(a_dictionary.items())
    for key, values in my_dict:
        print(f"{key}: {values}")
