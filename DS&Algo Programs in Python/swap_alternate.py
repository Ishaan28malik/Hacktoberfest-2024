def swapAlternate(arr, n):
    length=len(arr)
    if n%2==0:
        for i in range(0,length,2):
            arr[i],arr[i+1]=arr[i+1],arr[i]
    else:
         for i in range(0,length-1,2):
            arr[i],arr[i+1]=arr[i+1],arr[i]
    return

#Printing the array/list
def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(input())

while t > 0 :
    n = int(input())
    arr = []

    for i in range(0, n):
        ele = int(input())
        arr.append(ele) 
        
    if n != 0 :
        swapAlternate(arr, n)
        printList(arr, n)
    t -= 1