#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    
    leftDiagonalVal = 0
    rightDiagonalVal = 0
    
    #get the length of the matrix, since its square either the row or column will do
    length = len(arr)
    #get the top left to bottom right values
    for i in range(len(arr)):
       #get the top left to bottom right diag vals
       leftDiagonalVal += arr[i][i]
       #get the top right to bottom left diag vals
       # len of the array - row position - 1 to account for the length being +1 
       rightDiagonalVal += arr[i][length - i - 1]
       
    return abs(leftDiagonalVal - rightDiagonalVal)         
            
   
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
