#!/usr/bin/python3
"""
Fetch and display the body of a URL's response.
"""

if __name__ == "__main__":
    import sys
    from urllib import request, error

    url = sys.argv[1]

    try:
        with request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except error.HTTPError as http_err:
        print("Error code:", http_err.code)
