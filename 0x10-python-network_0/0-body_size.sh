#!/bin/bash
# Retrieve URL content with curl, count the bytes in the response body
curl -s "$1" | { read -r body; echo "${#body}"; }
