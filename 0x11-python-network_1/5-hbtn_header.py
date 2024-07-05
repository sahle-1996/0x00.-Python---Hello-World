#!/usr/bin/python3
"""
Fetches and displays the X-Request-Id from the URL's response header.
"""
import requests
import sys

if __name__ == '__main__':
    response = requests.get(sys.argv[1])
    print(response.headers.get('X-Request-Id'))
