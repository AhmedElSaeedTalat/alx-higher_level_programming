#!/usr/bin/python3
""" function that creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """load_from_json_file(filename): creates an Object from a JSON file"""
    with open(filename, "r", encoding="utf8") as f:
        data = json.load(f)
    return data
