# QUICK SORT : divide and conquer algorithm which picks an element of an arrays as pivot and partitions the 
# given array around the pivot i.e. put all elements smaller than pivot before it and all elements greater than pivot after it

# pivot can be selected inmany ways like it can be first element of array, last element of array or any random element

# In code below pivot is taken as last element of array

def partition(arr,low,high): 
    i = ( low-1 ) 
    pivot = arr[high] # pivot element 

    for j in range(low , high): 

        if arr[j] < pivot: 
        
            # increment index of smaller element 
            i = i+1
            arr[i],arr[j] = arr[j],arr[i] 

    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    if low < high: 

        ind = partition(arr,low,high) 

        # sort elements before partition and after partition 
        quickSort(arr, low, ind-1) 
        quickSort(arr, ind+1, high) 

arr = [5, 21, 11, 83, 45, 31] 
n = len(arr)

quickSort(arr,0,n-1) 

print ("Sorted array is :", *arr, end=" ") 

# Time Complexity O(N^2) [Worst Case] and O(NlogN) [Best Case]
