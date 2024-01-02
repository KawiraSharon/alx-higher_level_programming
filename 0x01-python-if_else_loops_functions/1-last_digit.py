#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    lastNo = number % 10
else:
    lastNo = (-number % 10) * -1

subline = f"Last digit of {number} is {lastNo}"

if lastNo > 5:
    print(f"{subline} and is greater than 5")
elif lastNo == 0:
    print(f"{subline} and is 0")
else:
    print(f"{subline} and is less than 6 and not 0")
