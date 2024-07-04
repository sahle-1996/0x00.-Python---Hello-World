#!/bin/bash
# Sends a GET request to a URL with curl and displays the body of the response (200 status code only)

response=$(curl -sL -w "%{http_code}" "$1")

# Check if the response code is 200
if [[ $response == *"200"* ]]; then
    curl -sL "$1" | grep -o 'Rout 2'
fi
