#!/usr/bin/python3
# Display header X-Request-Id.
import urllib.request
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        r = response.info()
        print(r['X-Request-Id'])
