#Selection Sort in Python
def selectionSort(arr):
    #the outer loop will traverse through all the element starting from the 0th index to n-1
    for i in range(0, len(arr)-1):
        #minimum value is initialized to i that everytime checks for the minimum value in the unsorted list of 'i'
        min_elem = i
        #the inner loop starts from i+1 as it iterates through the unsorted part of the list 
        for j in range(i+1, len(arr)):
            #we do comparison to find the minimum element in the remaining unsorted list
            if arr[j] < arr[min_elem]:
                #after finding the minimum value we assign it to the variable min_elem
                min_elem = j
        #swapping the minimum found element with the first element
        temp = arr[i]
        arr[i] = arr[min_elem]
        arr[min_elem] = temp
        
#taking input from user separated by delimiter                
inp = input('Enter a list of numbers separated by commas: ').split(',')
#typecasting each value of the list into integer
arr = [int(num) for num in inp]
selectionSort(arr)
print('The Sorted list is :',arr)
