#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to it, and displays the body of
the response. Prints an error code if the HTTP status is 400 or above.
"""
import requests
import sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
