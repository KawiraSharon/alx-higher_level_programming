#!/usr/bin/python3
"""
POST request to the passed URL with the email as a parameter
"""
import urllib.request
import urllib.parse
from sys import argv


def main(argv):
    """
    Sends a POST request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)
    """
    if len(argv) < 3:
        print("Usage: ./script_name.py <URL> <email>")
        return

    url = argv[1]
    email = argv[2]

    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        result = response.read()
        print(result.decode('utf8'))

if __name__ == "__main__":
    main(argv)
