#!/usr/bin/python3
def uppercase(str):
    for j in range(len(str)):
        if ord(str[j]) >= 97 and ord(str[j]) < 123:
            letter = 32
        else:
            letter = 0
        print("{:c}".format(ord(str[j]) - letter), end='')
    print()
