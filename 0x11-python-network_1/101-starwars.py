#!/usr/bin/python3
# Star wars API
import requests
import sys


if __name__ == "__main__":

    arg = sys.argv[1]
    value = {'search': arg}
    result = requests.get("https://swapi.co/api/people/?",
                          params=value)

    dict_data = result.json()
    print("Number of results: {}".format(dict_data.get("count")))
    for i in dict_data.get("results"):
        print(i.get('name'))
    while dict_data.get("next") is not None:
        result = requests.get(dict_data.get("next"), params=value)
        dict_data = result.json()
        for i in dict_data.get("results"):
            print(i.get('name'))
