#!/usr/bin/python3
"""
The module uses request to fetch https://intranet.hbtn.io/status
"""
import requests


def main():
    """
    Definition of function to fetch https://intranet.hbtn.io/status
    """
    url = 'https://intranet.hbtn.io/status'
    r = requests.get(url)
    print('Body response:')
    print('\t- type: {}'.format(type(r.text)))
    print('\t- content: {}'.format(r.text))

if __name__ == "__main__":
    main()
