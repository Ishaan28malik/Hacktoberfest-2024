def partition(array, start , end):
    i = (start-1)
    node = array[end]

    for j in range(start , end):
        if array[j] <= node:

            i = i+1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[end] = array[end], array[i+1]
    return (i+1)


def quickSort( array, start , end):
    if len(array) == 1:
        return array
    if start < end:

        pi = partition(array, start, end)


        quickSort(array,start,pi-1)
        quickSort(array,pi+1,end)


array = [ 98, 34, 28, 19, 3, 56, 48 ]
n = len(array)
quickSort(array, 0, n-1)
print("After Quick Sort\n")
print("Sorted array is :")
for i in range(n):
    print("%d" % array[i])        
