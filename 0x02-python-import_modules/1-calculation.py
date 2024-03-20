#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5
    operations = [
        ("+", add),
        ("-", sub),
        ("*", mul),
        ("/", div)
    ]

    for op_symbol, op_func in operations:
        print(f"{a} {op_symbol} {b} = {op_func(a, b)}")
