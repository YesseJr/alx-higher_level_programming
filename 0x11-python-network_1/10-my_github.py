#!/usr/bin/python3
"""
Display your id using the GitHub API.
"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    print(requests.get(https://api.github.com/user, auth=HTTPBasicAuth(argv[1], argv[2])).json().get('id'))
