#!/usr/bin/python3
"""This will ist the 10 most recent commits on a given GitHub repo.
Usage: ./100-github_commits.py <repository name> <repository owner>
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    req = requests.get(url)
    my_commits = req.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                my_commits[i].get("sha"),
                my_commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
