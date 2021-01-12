#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    
    #default the val to zero
    arrayTotal = 0
    
    if len(ar) < 1 or len(ar) > 10:
        print("out of constraint range")
        exit() 
    
        
    for i in range(len(ar)):
        
        #convert the array val to an int
        #ar_long = int(ar[i])
        if ar[i] < 0 or ar[i] > 10**10 :
            print("out of constraint range")
            exit()
        else:
            arrayTotal = arrayTotal + ar[i]    
            
    return arrayTotal;        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
