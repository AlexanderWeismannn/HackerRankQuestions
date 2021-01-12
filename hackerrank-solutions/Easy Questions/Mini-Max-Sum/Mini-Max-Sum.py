#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    
    #built in sorting method used by python to sort in ascending order
    arr.sort()  
    #print the sum of the first 4 ints and then the reverse    
    print("{} {}".format(sum(arr[:4]),sum(arr[-4:])))        
    

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
