#!/usr/bin/python3
def reverse(string):
    string = string[::-1]
    return string


list = []

for num in range(100):
    if num != 0 and num % 11 != 0:
        temp = "{:02d}".format(num)
        if reverse(temp) not in list:
            list.append(temp)

for item in list:
    print(item)
