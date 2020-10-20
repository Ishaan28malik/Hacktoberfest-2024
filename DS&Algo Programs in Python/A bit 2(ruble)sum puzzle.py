n, sum = [int(x) for x in input().split()]

arr = [int(x) for x in input().split()]


def getPairsCount(arr, n, sum):
    m = [0] * 1000
    for i in range(0, n):
        m[arr[i]] += 1
    twice_count = 0
    for i in range(0, n):
        twice_count += m[sum - arr[i]]
        if sum - arr[i] == arr[i]:
            twice_count -= 1

    # return the half of twice_count
    return int(twice_count / 2)


c = getPairsCount(arr, n, sum)
if c > 0:
    print("YES")
else:
    print("NO")
# count = 0
# for i in range(len(arr)):
#     j = i + 1
#     while j < len(arr):
#
#         if arr[i] + arr[j] == k:
#             count += 1
#         j += 1
# if count > 0:
#     print("YES")
# else:
#     print("NO")
