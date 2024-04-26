#!/usr/bin/python3
"""
Display value of X-Request-Id variable from header of response.
"""
import urllib.request
from sys import argv


def main(argv):
    """
    Method that take URL, send request to URL, display value of X-Request-Id variable
    """
    url = argv
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        print(headers['X-Request-Id'])

if __name__ == "__main__":
    main(argv[1])
