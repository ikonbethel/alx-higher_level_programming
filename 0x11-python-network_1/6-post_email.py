#!/usr/bin/python3
# Display the status
import requests
import sys


if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]
    value = {'email': email}
    result = requests.post(url, data=value)
    print(result.text)
