#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str_num = str(number)
last = int(str_num[-1])
temp = f"Last digit of "
if number < 0:
    last = -last
if last > 5:
    print(temp, number, " is ", last, " and is greater than 5")
elif last == 0:
    print(temp, number, " is ", last, " and is 0")
elif last < 6 and last != 0:
    print(temp, number, " is ", last, " and is less than 6 and not 0")
