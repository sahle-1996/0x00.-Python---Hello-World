#!/bin/bash
# Fetch URL content with curl, output body only if status code is 200
curl -s -o /dev/null -w "%{http_code}" "$1" | grep -q "^200$" && curl -s "$1"
