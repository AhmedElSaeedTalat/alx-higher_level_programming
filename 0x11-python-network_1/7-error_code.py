#!/usr/bin/python3
""" sends a POST request to the passed URL with the email as a parameter"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)
    print('Error code:', res.status_code)
