#!/usr/bin/python3
"""Script that fetches a URL and displays the X-Request-Id from response headers."""

from urllib import request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = request.Request(url)
    with request.urlopen(req) as res:
        headers = res.getheaders()
        print(dict(headers).get("X-Request-Id"))
