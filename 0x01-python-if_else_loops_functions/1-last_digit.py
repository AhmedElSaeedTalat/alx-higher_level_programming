#!/usr/bin/python3
import random
import math
number = random.randint(-10000, 10000)
if (math.fmod(number, 10)) > 5:
    print(f"Last digit of {number:d} is {number % 10:d} and is greater than 5")
elif (math.fmod(number, 10)) < 6 and (math.fmod(number, 10)) != 0:
    print(f"Last digit of {number:d} is {int(math.fmod(number, 10)):d} and\
 is less than 6 and not 0")
else:
    print(f"Last digit of {number:d} is {number % 10:d} and is 0")
