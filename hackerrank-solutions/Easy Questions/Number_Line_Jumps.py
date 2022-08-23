

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#  21 6 47 3
def kangaroo(x1, v1, x2, v2):

    #quickly check for edge cases
    if v1 == v2 and x1 == x2:
        return "YES"
    elif v1 == v2:
        return "NO"
    
    #derived from x1 + n*v1 = x2 + n*v2 solving for n.
    #the above equation represents the relation between the two kangaroos
    n = (x2 - x1)/(v1-v2)
    
    if (n > 0 and n%1 == 0):
        return "YES"
    else:
        return "NO"    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
