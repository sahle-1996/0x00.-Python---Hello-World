#!/usr/bin/python3
def pow(a, b):
    return a if b == 1 else a * pow(a, b - 1)
