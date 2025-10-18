#!/bin/python3

import math
import os
import random
import re
import sys

def DecimalToBinary(n):

    if(n>1):
            if(n%2==0):
                binary.append(0)
                DecimalToBinary(n/2)
            else:
                binary.append(1)
                n=n-1
                DecimalToBinary(n/2)
    elif(n==1):
        binary.append(1)

    else:
        binary.append(0)


if __name__ == '__main__':
    n = int(input())
    binary = [] 
    DecimalToBinary(n)
    print(binary)
    conse(binary)

