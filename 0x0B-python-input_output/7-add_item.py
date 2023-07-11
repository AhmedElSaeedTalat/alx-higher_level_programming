#!/usr/bin/python3
""" adds all arguments to a Python list"""
import json
import sys
import os
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

data = []
file_name = "add_item.json"
if os.path.exists(file_name):
    data = load_from_json_file(file_name)
if len(sys.argv) > 1:
    i = 1
    while i < len(sys.argv):
        data.append(sys.argv[i])
        i += 1
save_to_json_file(data, file_name)
