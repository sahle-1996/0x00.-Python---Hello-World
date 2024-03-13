#!/usr/bin/python3
def uppercase(s):
    for char in s:
        char_code = ord(char)
        if 97 <= char_code <= 122:
            char_code -= 32
        print("{:c}".format(char_code), end="")
    print()
