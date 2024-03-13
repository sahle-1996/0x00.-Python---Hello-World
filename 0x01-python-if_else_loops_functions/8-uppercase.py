#!/usr/bin/python3
def uppercase(s):
    for char in s:
        num = 32 if 'a' <= char <= 'z' else 0
        print(chr(ord(char) - num), end='')
    print()
