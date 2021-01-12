#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    arrLength = len(arr)
    posTotal = 0
    negTotal = 0
    zeroTotal = 0
    for i in range(arrLength):
        if arr[i] > 0:
           posTotal += 1 
        elif arr[i] < 0:
            negTotal += 1
        else:    
            zeroTotal += 1
    
    print("{:.6f}".format(posTotal/arrLength))
    print("{:.6f}".format(negTotal/arrLength))
    print("{:.6f}".format(zeroTotal/arrLength))
   
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
