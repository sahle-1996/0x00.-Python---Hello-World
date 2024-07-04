#!/bin/bash
# GET method using curl and display body of a 200 status code response

# Send GET request and capture both output and HTTP status
response=$(curl -sL -w "%{http_code}" "$1")

# Extract the HTTP status code
status_code="${response: -3}"

# Display body only if status code is 200
[ "$status_code" == "200" ] && curl -sL "$1"
