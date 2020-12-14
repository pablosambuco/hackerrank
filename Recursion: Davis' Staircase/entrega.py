#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.
def stepPerms(n,m=3):
    tot=0
    for x in rec(n,m):
        n=1
        i=0
        l=0
        while i<m:
            if x[1] > 0:
               l+=x[1]
               n*=math.factorial(l)/(math.factorial(l-x[1])*math.factorial(x[1]))
            x=x[3]
            i+=1
        tot+=n
    return int(tot)%10000000007  

def rec(n,m):
    res=[]
    a=int(n/m)
    i=0
    if m == 1:
       res.append([n,n,m,[]])
    else:
        while i<=a:
            r=n- i*m
            for x in rec(r,m-1):
                res.append([n,i,m,x])
            i+=1
    return res
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())
        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
