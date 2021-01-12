#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    
    width = len(word)
    height = 0
    
    alphabetDict = {
        "a": h[0], "b": h[1], "c": h[2],
        "d": h[3], "e": h[4], "f": h[5],
        "g": h[6], "h": h[7], "i": h[8],
        "j": h[9], "k": h[10], "l": h[11],
        "m": h[12], "n": h[13], "o": h[14],
        "p": h[15], "q": h[16], "r": h[17],
        "s": h[18], "t": h[19], "u": h[20],
        "v": h[21], "w": h[22], "x": h[23],
        "y": h[24], "z": h[25]    
    }
    
    for i in range(len(word)):
       if alphabetDict.get(word[i]) > height:
        height = alphabetDict.get(word[i])
    
    area = width * height
    return area

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()