# Given an array arr of N integers
# Find the contiguous sub-array with maximum sum

def max_subarray_sum(arr):
    # if there is no positive element in the array
    if max(arr) < 0:
        return max(arr)

    mxm = max_end = 0
    length = len(arr)
    for i in range(length):
        max_end += arr[i]
        if mxm < max_end:
            mxm = max_end
        if max_end < 0:
            max_end = 0
    return mxm

'''for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))'''

# a = [1, 2, 3, -2, 5]
a = [-1, -2, -3, -4]
print(max_subarray_sum(a))
