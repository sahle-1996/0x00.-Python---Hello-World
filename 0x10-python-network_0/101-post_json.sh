#!/bin/bash
# POST method using curl to send JSON data
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"
