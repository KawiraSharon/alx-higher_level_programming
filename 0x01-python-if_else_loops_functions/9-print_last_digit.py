#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        lastNo = number % 10
    else:
        lastNo = number % -10
        lastNo *= -1

    print("{:d}".format(lastNo), end='')
    return (lastNo)
