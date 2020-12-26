#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    acount = 0
    ls = len(s)
    if ls == 1:
        return n
    i = 0
    while i < ls:
        if s[i] == "a":
            acount += 1
        i += 1
    acount *= int(n/ls)
    i = 0
    while i < n % ls:
        if s[i] == "a":
            acount += 1
        i += 1
    return acount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
