#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    
    for i in range(len(grades)):
        #check to make sure that the value is greater than a failing grade no matter what
        if(grades[i] >= 38):
            #check if the difference of the next multiple of 5 - the value < 3 
            if((( grades[i] - (grades[i]%5) + 5) - grades[i]) < 3 ):
                #if yes then set the value to the next multiple of 5
               grades[i] = (grades[i] - (grades[i]%5)) + 5
               
    return grades           
                    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()