#!/usr/bin/python3
# Display error
import urllib.request
import sys


if __name__ == "__main__":

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            r = response.read()
            print(r.decode('utf-8'))
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.status))
