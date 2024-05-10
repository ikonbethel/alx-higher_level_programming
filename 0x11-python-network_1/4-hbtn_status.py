#!/usr/bin/python3
# Display the status.
import requests

if __name__ == "__main__":

    result = requests.get('https://intranet.hbtn.io/status')
    r = result.text
    print("Body response:")
    print("\t- type: {}".format(type(r)))
    print("\t- content: {}".format(r))
