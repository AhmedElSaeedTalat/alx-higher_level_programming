#!/usr/bin/python3
""" sends a request to the URL and displays the body of the response"""
from urllib.request import urlopen
from urllib.error import HTTPError
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urlopen(url) as f:
            res = f.read().decode('utf8')
            print(res)
    except HTTPError as e:
        print('Error code:', e.code)
