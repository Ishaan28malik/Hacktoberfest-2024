# sort
def insertion_sort(arr):
   for i in range(1, len(arr)):
      temp = arr[i]
      pos = binary_search(arr, temp, 0, i) + 1
      for k in range(i, pos, -1):
         arr[k] = arr[k - 1]
      arr[pos] = temp
def binary_search(arr, key, start, end):
   #key
   if end - start <= 1:
      if key < arr[start]:
         return start - 1
      else:
         return start
   mid = (start + end)//2
   if arr[mid] < key:
      return binary_search(arr, key, mid, end)
   elif arr[mid] > key:
      return binary_search(arr, key, start, mid)
   else:
      return mid
# main
arr = [1,5,3,4,8,6,3,4]
n = len(arr)
insertion_sort(arr)
print("Sorted array is:")
for i in range(n):
   print(arr[i],end=" ")
