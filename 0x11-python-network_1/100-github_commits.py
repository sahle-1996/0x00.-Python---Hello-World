#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve the given challenge
"""
import requests
from sys import argv

if __name__ == '__main__':
    repo = argv[1]
    owner = argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    try:
        response = requests.get(url)
        response.raise_for_status()
        commits = response.json()
        for commit in commits[:10]:
            print(f"{commit['sha']}: {commit['commit']['author']['name']}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
