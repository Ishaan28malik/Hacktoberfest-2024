# BUBBLE SORT : repeatedly swaps adjacent elements if they are in wrong order i.e if we want to sort array in ascending order
# then if adjacent elements are not in ascending order then we swap them

def bubbleSort(arr): 
    
    n = len(arr) 

    for i in range(n): 
 
        for j in range(0, n-1): 

            # swap if the element found is greater than the next element 
            
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 

arr = [20, 121, 17, 3, 99, 56, 11] 

bubbleSort(arr) 

print ("Sorted array is : ", end=" ") 
for i in range(len(arr)): 
    print(arr[i], end=" ") 

# Time Complexity : O(N^2)
# Space Complexity : O(1)