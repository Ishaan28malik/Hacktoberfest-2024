"""
Given an array of distinct integers, 
find length of the longest subarray which contains numbers that can be arranged in a continuous sequence.


Examples:

Input:  arr[] = {10, 12, 11};
Output: Length of the longest contiguous subarray is 3

Input:  arr[] = {14, 12, 11, 20};
Output: Length of the longest contiguous subarray is 2

Input:  arr[] = {1, 56, 58, 57, 90, 92, 94, 93, 91, 45};
Output: Length of the longest contiguous subarray is 5
"""

def find_length(arr):

    arr.sort()
    n = len(arr)

    long_len = 1
    result = []

    start = 0

    while start < n-1:

        if arr[start] == arr[start+1] - 1:
            long_len += 1
        else:
            result.append(long_len)
            long_len = 1
        start += 1
    
    result.append(long_len)

    if max(result) != 1:
        return max(result)
    else:
        return -1

# A = [1, 56, 58, 57, 90, 92, 94, 93, 91, 45]
# A = [10, 12, 11]
A = [15, 13, 11, 20]
print(find_length(A))
