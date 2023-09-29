#!/usr/bin/python3
""" post a letter """
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""
    url = 'http://0.0.0.0:5000/search_user'
    val = {'q': letter}
    res = requests.post(url, data=val)
    header = res.headers.get('content-type')
    if header == 'application/json':
        try:
            js = res.json()
            if len(js) > 0:
                print(f"[{js['id']}]", js['name'])
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
