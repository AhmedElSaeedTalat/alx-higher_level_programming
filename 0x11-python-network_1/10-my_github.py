#!/usr/bin/python3
""" post a letter """
import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    usr = sys.argv[1]
    ps = sys.argv[2]
    res = requests.get(url, auth=(usr, ps))
    res = res.json()
    try:
        print(res['id'])
    except KeyError:
        print('None')
