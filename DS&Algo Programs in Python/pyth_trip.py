'''Given an array arr of N integers
write a function that 
returns true if there is a triplet (a, b, c) 
that satisfies a2 + b2 = c2
otherwise false'''

import math

def checkTriplet(arr, n):
    mxm = 0

    # finding maximum element
    for element in arr:
        mxm = max(mxm, element)
    
    # hashing array
    hash = [0]*(mxm+1)

    for element in arr:
        hash[element] += 1

    for i in range(1, mxm+1):
        if hash[i] == 0:
            continue

        for j in range(1, mxm+1):
            if (i==j and hash[i]==1) or hash[j]==0:
                continue

            val = int(math.sqrt(i*i+j*j))
            if val*val != (i*i+j*j):
                continue
            if val>mxm:
                continue
            if hash[val]:
                return True
    return False

'''n = int(input())
a = list(map(int,input().split()))'''

N = 5
Arr = [3, 2, 4, 6, 5]

# N = 3
# Arr = [3, 8, 5]

if checkTriplet(Arr, N):
    print("Yes")
else:
    print("No")
