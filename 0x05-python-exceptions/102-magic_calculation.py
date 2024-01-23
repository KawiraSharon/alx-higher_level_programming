#!/usr/bin/python3

def magic_calculation(a, b):
    """does exactly as the provided bytecode"""
    result = 0
    for idx in range(1, 3):
        try:
            if idx > a:
                raise Exception("Too far")
            else:
                result += (a**b) / idx
        except Exception:
            result = a + b
            break
    return result
