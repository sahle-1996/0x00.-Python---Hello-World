#!/usr/bin/python3
import random

number = random.randint(-10, 10)

outcome = (
    f"{number} is positive" if number > 0 else
    f"{number} is zero" if number == 0 else
    f"{number} is negative"
)

print(outcome)
