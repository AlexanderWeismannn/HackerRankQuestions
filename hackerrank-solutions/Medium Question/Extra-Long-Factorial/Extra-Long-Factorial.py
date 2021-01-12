#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    # for some reason i cant use return on this question
    # so instead of just using recursion i have to do this
    # janky for loop
    factorial = 1
    for i in range(1,n+1):
        factorial *= i
        
    print(factorial)    
    
if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
