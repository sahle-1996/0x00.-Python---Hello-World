#!/usr/bin/python3
def pow(a, b):
    return exp_recursive(a, b)


def exp_recursive(a, b):
    if b == 0:
        return 1
    elif b < 0:
        return 1 / (a * exp_recursive(a, -b - 1))
    else:
        return a * exp_recursive(a, b - 1)
