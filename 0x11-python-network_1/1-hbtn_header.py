#!/usr/bin/python3
""" displays the value of the X-Request-Id """
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as f:
        headers = f.getheaders()
        for header in headers:
            if header[0] == 'X-Request-Id':
                print(header[1])
                break
