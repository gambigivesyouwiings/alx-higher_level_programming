#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError as typ:
        sys.stderr.write(f"Exception: {typ}\n")
        return False
    else:
        return True
