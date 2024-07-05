#!/usr/bin/python3
"""
Script that takes in a URL and an email, sends a POST request, and displays
the body of the response.
"""
import sys
import requests

if __name__ == "__main__":
    url, email = sys.argv[1], sys.argv[2]
    response = requests.post(url, data={'email': email})
    print(response.text)
