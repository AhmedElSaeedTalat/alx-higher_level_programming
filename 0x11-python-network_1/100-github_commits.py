#!/usr/bin/python3
""" fetch last 10 commits """
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    per_page = 10
    query_params = f'sort=committer-date&per_page={per_page}'
    url = f'https://api.github.com/repos/{owner}/{repo}/commits?{query_params}'
    req = requests.get(url)
    res = req.json()
    for i in res:
        print(f"{i['sha']}:", i['commit']['author']['name'])
