#!/usr/bin/python3
""" get a status code """
import requests
import sys
from requests.exceptions import HTTPError


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        res = requests.get(url)
        print(res.text)
    except HTTPError as e:
        print('Error code:', res.status_code)
