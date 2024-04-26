#!/usr/bin/python3
"""
Script to fetch https://intranet.hbtn.io/status
"""
import urllib.request


def main():
    """
    Function that prints response of url that is specific.
    """
    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode('utf8')))

if __name__ == "__main__":
    main()
