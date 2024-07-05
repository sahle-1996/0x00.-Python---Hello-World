#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
import sys

if __name__ == '__main__':
    q = sys.argv[1] if len(sys.argv) == 2 else ""
    url = 'http://0.0.0.0:5000/search_user'
    try:
        response = requests.post(url, data={'q': q})
        json_data = response.json()

        if isinstance(json_data, dict) and json_data:
            id = json_data.get('id')
            name = json_data.get('name')
            if id and name:
                print(f"[{id}] {name}")
            else:
                print("No result")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
    except Exception as e:
        print(f"Error: {e}")
