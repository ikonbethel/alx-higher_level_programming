#!/usr/bin/python3
# Star wars API
import requests
import sys


if __name__ == "__main__":

    repo = sys.argv[1]
    owner = sys.argv[2]
    result = requests.get("https://api.github.com/repos/{}/{}/commits".
                          format(owner, repo))

    dict_json = result.json()
    if len(dict_json) > 10:
        n = 10
    else:
        n = len(dict_json)
    for j in range(n):
        i = dict_json[j]
        print("{}: {}".format(i.get('sha'), i.get('commit').
              get('author').get('name')))
