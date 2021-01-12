#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    
    
    
    #comparisonList[0] = a's score and comparisonList[1] = b's score
    comparisonList = [0,0]
    
    for i in range(len(b)):
        #make sure that the values are within the constraints
        if a[i] < 1 or a[i] > 100 or b[i] < 1 or b[i] > 100:
            
            print("Data entered out of allowable range")
            exit()
        else:
            if a[i] > b[i]:
                comparisonList[0] = comparisonList[0] + 1   
            elif a[i] < b[i]:
                comparisonList[1] = comparisonList[1] + 1
            #else the are equal and nothing needs to be done    
        
    return comparisonList        
                
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()