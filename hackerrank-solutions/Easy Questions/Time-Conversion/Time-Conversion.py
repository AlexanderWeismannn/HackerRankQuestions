#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    # Write your code here.
    enteredTime = s.split(":")
    PM = "PM"
    
    #the time is PM
    if PM in enteredTime[2]:
        #make sure its not 12 pm 
        if enteredTime[0] != "12":
            enteredTime[0] = str(int(enteredTime[0])+12)
    #it is AM        
    else:  
        if enteredTime[0] == "12": 
            enteredTime[0] = "00" 
    
            
    #rejoin the array together 
    returnTime = ":".join(enteredTime) 

    #return everythinge except the end two characters (AM/PM)
    return returnTime[:-2]


    
   
    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()