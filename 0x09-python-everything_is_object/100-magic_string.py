#!/usr/bin/python3
def magic_string(string=None):
    if string is None:
        string = []
    string.append('BestSchool')
    result = ', '.join(string)
    print(result)
