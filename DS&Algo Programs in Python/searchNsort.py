'''
11. Write a menu-driven program to accept a list of student names and perform
the following
a. search an element using linear search/ binary search.
b. Sort the elements using bubble sort/ insertion sort/ selection sort.
'''

def input_list():
    l = []
    n = int(input("\nEnter the number of students: "))
    for i in range(0, n, 1):
        l.append(input(f"Enter the name {i+1}: ").lower())

    return n, l

def linear_Search(n, l):
    '''
    Performs linear search algorithm.
    Parameters: n -> length of list
                l -> list
    '''
    x = input("\nEnter the name to be searched: ").lower()
    flag = False
    for i in range(0, n, 1):
        if l[i] == x:
            flag = True
            break
        
    if flag == True:
        print("\nElement found at position", i+1)
    else:
        print("\nElement not found!")

def binary_search(n, l):
    '''
    Performs binary search algorithm.
    Parameters: n -> length of list
                l -> list
    '''
    l = bubble_sort(n, l.copy())
    flag = False
    x = input("\nEnter the name to be searched: ").lower()
    lb, ub = 0, n-1
    
    while lb <= ub:
        mid = (lb+ub)//2
        if x == l[mid]:
            flag = True
            break
        if x < l[mid]:
            ub = mid - 1
        if x > l[mid]:
            lb = mid + 1
    
    if flag == True:
        print("\nElement found!")
    else:
        print("\nElement not found!")

def bubble_sort(n, l1):
    '''
    Time Complexity: O(n^2)
    Parameters: n -> length of list
                l1 -> list
    Return: l1 -> sorted list
    '''
    for i in range(0, n, 1):
        for j in range(0, n-i-1, 1):
            if l1[j] > l1[j+1]:
                l1[j], l1[j+1] = l1[j+1], l1[j]
    
    return l1

def insertion_sort(n, l1):
    '''
    Algorithm
    To sort an array of size n in ascending order:
    1: Iterate from arr[1] to arr[n] over the array.
    2: Compare the current element (key) to its predecessor.
    3: If the key element is smaller than its predecessor,
        compare it to the elements before.
        Move the greater elements one position up to make
        space for the swapped element.
    Time Complexity: O(n^2)
    Parameters: n -> length of list
                l1 -> list
    '''
    for i in range(1, n, 1):
        key = l1[i]
        j = i-1
        while j>=0 and key<l1[j]:
            l1[j+1] = l1[j]
            j -= 1
        l1[j+1] = key
    else:
        print("\nInsertion Sorted List:", l1)

def selection_sort(n, l1):
    '''
    The algorithm maintains two subarrays in a given array.
    1) The subarray which is already sorted.
    2) Remaining subarray which is unsorted.
    In every iteration of selection sort, the minimum element
    from the unsorted subarray is picked and moved to the sorted subarray.
    Time Complexity: O(n^2) as there are two nested loops.
    Parameters: n -> length of list
                l1 -> list
    '''
    for i in range(0, n, 1):
        minim = i
        for j in range(i+1, n, 1):
            if l1[minim]>l1[j]:
                minim = j
        l1[i], l1[minim] = l1[minim], l1[i]
    else:
        print("\nSelection Sorted List:", l1)

search_switcher = {
                    1: linear_Search,
                    2: binary_search
                  }

sort_switcher = {
                    1: bubble_sort,
                    2: insertion_sort,
                    3: selection_sort
                }

def main(n, l):
    
    print("\n========= Menu =========")
    print("1. Search an element\
         \n2. Sort the elements\
         \n0. Exit")

    ch = int(input("\nEnter you choice: "))
    if ch == 1:
        print("\n========= Searching Menu =========")
        print("1. Linear Search\
                \n2. Binary Search")
        choice = int(input("\nEnetr your choice: "))
        func = search_switcher.get(choice, lambda n,l: print("\nInvlaid Choice!"))
        func(n, l)
    elif ch == 2:
        print("\n========= Sorting Menu =========")
        print("1. Bubble Sort\
                \n2. Insersion Sort\
                \n3. Selection Sort")
        choice = int(input("\nEnter your choice: "))
        func = sort_switcher.get(choice, lambda n,l: print("\nInvlaid Choice!"))
        if choice == 1:
            l1 = func(n, l.copy())
            print("\nBubble Sorted List:", l1)
        else:
            func(n,l.copy())
        
    elif ch == 0:
        exit()
    else:
        print("\nInvalid Choice!")

if __name__ == "__main__":
    n, l = input_list()
    while True:
        main(n, l)