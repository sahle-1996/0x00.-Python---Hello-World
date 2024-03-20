#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    a = 10
    b = 5
    result_add = calc.add(a, b)
    result_sub = calc.sub(a, b)
    result_mul = calc.mul(a, b)
    result_div = calc.div(a, b)
    print(f"{a} + {b} = {result_add}")
    print(f"{a} - {b} = {result_sub}")
    print(f"{a} * {b} = {result_mul}")
    print(f"{a} / {b} = {result_div}")
