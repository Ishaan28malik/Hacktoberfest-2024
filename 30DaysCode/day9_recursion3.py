#!/bin/python3
import os

def factorial(n):
    if 0 <= n <= 1:
        return 1
    elif 2 <= n <= 12:
        return n*factorial(n-1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    result = factorial(n)
    fptr.write(str(result) + '\n')
    fptr.close()
