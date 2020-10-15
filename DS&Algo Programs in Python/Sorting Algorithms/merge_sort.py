# MERGE SORT : divide and conquer algorithm in where array is repeatedly divided into two halves and then the two halves are sorted and merged

def merge_sort(arr): 

    if len(arr)>1: 
        
        m = len(arr)//2
        
        left = arr[:m]  # two halves of arr
        right = arr[m:] 
        
        # recurrsive calling for two halves
        
        left = merge_sort(left) 
        right = merge_sort(right) 

        arr =[] 

        while len(left)>0 and len(right)>0: 
            
            if left[0]<right[0]: # comparing first elements of two halves
                arr.append(left[0]) 
                left.pop(0) 
            else: 
                arr.append(right[0]) 
                right.pop(0) 

        for i in left: 
            arr.append(i) 
        for i in right: 
            arr.append(i) 
                
    return arr 

a = [24, 3, 77, 45, 99, 19, 55]

sorted_a = merge_sort(a) 

print("Sorted array is :", end=" ") 
print(*sorted_a) 

# Time Complexity : T(n) = T(n/2)+f(n) is recurrce relation and f(n) varies with machine
# Space Complexity : O(N)