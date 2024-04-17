#!/usr/bin/python3
"""
Module: 0-read_file
Reads from a file and prints its contents.
"""


def read_file(filename=""):
    """
    Read from filename and print its contents to stdout.
    Args:
        filename (str): Name of the file to read.
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
