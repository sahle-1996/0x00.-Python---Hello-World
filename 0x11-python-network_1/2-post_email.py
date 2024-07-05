#!/usr/bin/python3
"""Script that sends a POST request with an email to a URL and shows response."""

import sys
from urllib import request, parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    encoded_data = parse.urlencode(email).encode("utf-8")

    req = request.Request(url, encoded_data)
    with request.urlopen(req) as res:
        print(res.read().decode("utf-8"))
