#!/usr/bin/python3
j = 0
for ASCII in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(ASCII - j)), end='')
    j = 32 if j == 0 else 0
