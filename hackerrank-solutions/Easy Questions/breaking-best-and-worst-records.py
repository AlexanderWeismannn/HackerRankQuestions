import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # default high and low to be the first every score
    new_high = scores[0]
    new_low = scores[0]
    #counters for progressing through the list
    num_high = 0
    num_low = 0
    #loop through and do the logical high/low checks
    for s in scores:
        if s > new_high:
            new_high = s
            num_high += 1;
        elif s < new_low:
            new_low = s
            num_low += 1
            
    #return the values in list format            
    return [num_high,num_low]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
