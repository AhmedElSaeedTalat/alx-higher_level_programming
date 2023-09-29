#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request


url = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(url) as f:
    print('Body response:')
    res = f.read()
    print('\t-', 'type:', type(res))
    print('\t-', 'content:', res)
    print('\t-', 'utf8 content:', res.decode('utf8'))
