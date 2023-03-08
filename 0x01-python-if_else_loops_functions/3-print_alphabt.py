#!/usr/bin/python3
for a in range(97, 123):
    if a in [101, 113]:
        pass
    else:
        print("{:c}".format(a), end="")
