#!/usr/bin/python3
""" displays the value of the X-Request-Id """
from urllib.request import urlopen
import sys


url = sys.argv[1]
with urlopen(url) as f:
    headers = f.getheaders()
    for header in headers:
        if header[0] == 'X-Request-Id':
            print(header[1])
            break
