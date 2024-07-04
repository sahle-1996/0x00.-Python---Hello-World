#!/bin/bash
# DELETE method using curl
curl -s -I "$1" | awk '/Allow/ {print $2,$3,$4}'
