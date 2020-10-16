#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    if 2<=n<=20:
        #Print ten lines where 1<=i<=10, result = n*i
        for i in range(1,11):
            print('{} x {} = {}'.format(str(n),str(i),str(n*i)))
