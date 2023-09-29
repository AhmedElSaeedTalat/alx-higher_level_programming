#!/usr/bin/python3
""" post a letter """
import requests
import sys


if __name__ == "__main__":
    letter = sys.argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': letter}
    header = {"content-type":"application/json"}
    res = requests.post(url, data=data, headers=header)
    print(res.text)
