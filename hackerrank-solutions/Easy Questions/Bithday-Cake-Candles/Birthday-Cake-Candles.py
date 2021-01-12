#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    
    #candles are sorted in ascending order
    #candles.sort()
    
    candleHeight = 0
    sum = 0
    for i in range(len(candles)):
        
        #set a new height and give an initial sum value of 1
        if candles[i] > candleHeight:
            candleHeight = candles[i]
            sum = 1
        #they are the same height so in increase the value by 1    
        elif candles[i] == candleHeight:
            sum +=1
        #dont need to so anything if it is less than the current height    
    
    return sum
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()