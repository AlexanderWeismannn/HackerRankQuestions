import random
import re
import sys
from math import *

# Complete the encryption function below.
def encryption(s):
    #replace any spaces and get the length of the new string
    #s = s.replace(" ","")  
    L = len(s) 
    #number of rows
    row = floor(sqrt(L))
    #number of columns
    column = ceil(sqrt(L))
    
    #create a matrix to hold everything
    finalList = []
    
    #for loop to skip through the list based on column position
    for i in range(column):
        tempList = []
        j = 0
        
        #while not at the end of the list
        #add the characters to a temp list and increment by a column length 
        while i + j < L:
            tempList.append(s[i+j])
            j += column 
        finalList.append("".join(tempList))
        
    finalList = " ".join(finalList)
    return  finalList 
   
  
 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
