# INSERTION SORT : each element of array is picked up one by one and comared with all the preceeding elements until and unless
# its correct position is determined

def insertionSort(arr): 

    for i in range(1, len(arr)): 

        key = arr[i] 

        # elements greater than key are shifted ahead to make place for key
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 

arr = [12, 11, 94, 77, 24, 88, 43]
insertionSort(arr) 

print("Sorted Array : ", end=" ")

for i in range(len(arr)): 
    print(arr[i], end=" ") 

# Time Complexity : O(N^2)
# Space Coplexity : O(1)