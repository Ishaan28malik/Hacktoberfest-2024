# SELECTION SORT : Sorts an array by repeatedly finding the minimum element and from the unsorted portion 
# and inserting it at the beginning
 
arr = [32, 11, 7, 91, 45, 18] 

for i in range(len(arr)): 
    
    # finding the minimum element in remaining unsorted array 
    
    min_index = i 
    for j in range(i+1, len(arr)): 
        if arr[min_index] > arr[j]: 
            min_index = j 
            
    # swap the minimum element with the first element
    arr[i], arr[min_index] = arr[min_index], arr[i] 

print ("Sorted array : ", end=" ") 
for i in range(len(arr)): 
    print(arr[i], end=" ")
    
# Time Complexity : O(N^2)
# Space Complexity : O(1)