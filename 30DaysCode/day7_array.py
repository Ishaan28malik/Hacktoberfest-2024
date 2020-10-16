#!/bin/python3

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    print(' '.join(list(map(str,arr[::-1]))))
