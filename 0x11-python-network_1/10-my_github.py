#!/usr/bin/python3
# Star wars API
import requests
import sys


if __name__ == "__main__":

    usr = sys.argv[1]
    pwd = sys.argv[2]
    value = {usr: pwd}
    result = requests.get("https://api.github.com/user",
                          auth=requests.auth.HTTPBasicAuth(usr, pwd))

    if result.status_code < 400:
        dict_data = result.json()
        print(dict_data['id'])
    else:
        print(None)
