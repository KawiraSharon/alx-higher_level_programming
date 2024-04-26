#!/usr/bin/python3
"""
This code sends a request to URL then display body of response.
"""
import requests
from sys import argv


def main(argv):
    """
    This python method manages urllib.error.HTTPError exceptions
    It also prints the Error code: follows it with the HTTP status code
    """
    url = argv[1]
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))


if __name__ == "__main__":
    main(argv)
