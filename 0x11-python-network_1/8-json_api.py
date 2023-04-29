#!/usr/bin/python3
# Search API
import requests
import sys


if __name__ == "__main__":

    if len(sys.argv) != 1:
        letter = sys.argv[1]
    else:
        letter = ""
    value = {'q': letter}
    result = requests.post("http://0.0.0.0:5000/search_user", data=value)
    try:
        if "id" not in result.json() or "name" not in result.json():
            print("No result")
        else:
            print("[{}] {}".format(result.json().get('id'),
                  result.json().get('name')))
    except:
        print("Not a valid JSON")
