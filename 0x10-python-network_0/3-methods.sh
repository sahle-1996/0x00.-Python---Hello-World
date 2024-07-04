#!/bin/bash
# Display all HTTP methods the server will accept using curl
curl -s -I "$1" | grep -i "^allow:" | cut -d ' ' -f 2-
