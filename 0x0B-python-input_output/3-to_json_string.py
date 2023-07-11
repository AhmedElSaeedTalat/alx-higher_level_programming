#!/usr/bin/python3
""" returns the JSON representation of an object """
import json


def to_json_string(my_obj):
    """ def to_json_string(my_obj): jsonrepresentation """
    return json.dumps(my_obj)
