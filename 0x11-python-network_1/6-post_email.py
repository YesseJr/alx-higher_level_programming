#!/usr/bin/python3
"""
Takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter
"""
from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    payload = {'email': argv[2]}
    r = requests.post(url, data=payload)
    print(r.text)
