#!/usr/bin/python3

import calculator_1 as calc

a = 10
b = 5

summation = calc.add(a, b)
difference = calc.sub(a, b)
product = calc.mul(a, b)
divisor = calc.div(a, b)

print(f"{a} + {b} = {summation}")
print(f"{a} - {b} = {difference}")
print(f"{a} * {b} = {product}")
print(f"{a} / {b} = {divisor}")
