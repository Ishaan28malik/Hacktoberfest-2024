n = int(input())
arr = list(map(int,input().split()))
temp = [0]*(max(arr)+1)
for i in arr:
    temp[i] += 1
for j in range(1, len(temp)):
    temp[j] += temp[j-1]
output = [0] + arr
for i in range(len(arr)-1, -1, -1):
    output[temp[arr[i]]] = arr[i]
    temp[arr[i]] -= 1
arr = output[1:]
print(arr)
