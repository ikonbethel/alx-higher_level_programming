#!/usr/bin/python3
# Display header X-Request-Id
import requests
import sys


if __name__ == "__main__":

    url = sys.argv[1]
    result = requests.get(url)

    if result.status_code < 400:
        print(result.text)
    else:
        print("Error code: {}".format(result.status_code))
