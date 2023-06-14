#!/usr/bin/python3
def best_score(a_dictionary):
    score = -1
    if not a_dictionary:
        return None
    for key, value in a_dictionary.items():
        if value > score:
            score = value
    if score == -1:
        return None
    for key, value in a_dictionary.items():
        if score == value:
            return key
