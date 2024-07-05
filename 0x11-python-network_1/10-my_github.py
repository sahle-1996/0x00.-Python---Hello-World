#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
from sys import argv

if __name__ == '__main__':
    username = argv[1]
    token = argv[2]
    url = f'https://api.github.com/users/{username}'
    auth = (username, token)
    
    try:
        response = requests.get(url, auth=auth)
        if response.status_code == 200:
            user_data = response.json()
            print(user_data.get('id'))
        else:
            print(f"Error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
