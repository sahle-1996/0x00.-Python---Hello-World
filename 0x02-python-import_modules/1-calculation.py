#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a, b = 10, 5
    expressions = [
        ("{} + {} = {}", add(a, b)),
        ("{} - {} = {}", sub(a, b)),
        ("{} * {} = {}", mul(a, b)),
        ("{} / {} = {}", div(a, b))
    ]
    
    for expr in expressions:
        print(expr[0].format(a, b, expr[1]))
