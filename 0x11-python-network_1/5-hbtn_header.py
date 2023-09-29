#!/usr/bin/python3
""" sends a request to the URL and displays X-Request-Id"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)
    print(res.headers.get('X-Request-Id'))
