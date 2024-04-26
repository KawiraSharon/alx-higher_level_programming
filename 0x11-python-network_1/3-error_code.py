#!/usr/bin/python3
"""
this piece of code sends request to URL, then displays body of the response.
"""
import urllib.request
from sys import argv


def main(argv):
    """
    This method manages urllib.error.HTTPError exceptions
    It also prints: Error code: follows it with its-HTTP status code
    """
    url = argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            result = response.read()
            print(result.decode('utf8'))
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    main(argv)
