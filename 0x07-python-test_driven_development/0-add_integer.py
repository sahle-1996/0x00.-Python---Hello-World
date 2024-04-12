#!/usr/bin/python3
"""0. Integers addition"""


def add_integer(a, b=98):
    """
    Function that adds two integers
    Raise TypeError if a or b are not integers/floating points
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
