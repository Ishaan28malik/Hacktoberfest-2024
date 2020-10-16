'''
Implementation of Binary Search Algorithm in Python
'''
def bubblesort(arr):
        n = len(arr)
        print("original list:",arr)
        for i in range (n-1):
                for j in range(0,n-i-1):
                        if arr[j] > arr[j+1]:
                                arr[j], arr[j+1] = arr[j+1], arr[j]
        print("sorted list:",arr)
arr = []
num = int(input("enter number of elements:"))
for i in range(num):
        ele = int(input("enter elements:"))
        arr.append(ele)
bubblesort(arr)
                

