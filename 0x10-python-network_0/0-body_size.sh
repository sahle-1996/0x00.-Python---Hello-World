#!/usr/bin/env bash
# Script to fetch the URL and display the size of the response body in bytes

response=$(curl -s -D - "$1" -o /dev/null)
content_length=$(echo "$response" | grep -i "Content-Length" | awk '{print $2}')

if [ -n "$content_length" ]; then
    echo "$content_length"
else
    curl -s "$1" | wc -c
fi
