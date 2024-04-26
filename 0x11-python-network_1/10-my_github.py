#!/usr/bin/python3
"""
This module accesses the GitHub API and uses the information
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


def main(argv):
    """
    This script takes one's GitHub credentials (username and password) and
    uses the API of the platform to display their id.
    """
    user = argv[1]
    password = argv[2]
    response = requests.get('https://api.github.com/user',
                            auth=HTTPBasicAuth(user, password))
    try:
        profile_info = response.json()
        print(profile_info['id'])
    except:
        print('None')

if __name__ == "__main__":
    main(argv)
