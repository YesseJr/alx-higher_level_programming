#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the value of the X-Request-Id
"""
import sys
import urllib.request


if __name__ == "__main__":

    request = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
