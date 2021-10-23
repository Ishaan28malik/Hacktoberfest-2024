def mergeSort(arr, value):
    if (len(arr)) = 1:
        return arr, 0
    a, value1 = mergeSort(arr[:(len(arr)//2)], value)
    b, value2 = mergeSort(arr[:(len(arr)//2)], value)
    value = value1 + value2
    c = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1

        else:
            c.append(b[j])
            j += 1
            value += ((len(a)+len(b)//2) - i 
