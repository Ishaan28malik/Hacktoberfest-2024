def partition(arr, start, end):
    i=start-1
    pivot= arr[end]
    for j in range(start, end):
        if arr[j]<=pivot:
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
    arr[i+1],arr[end] = arr[end],arr[i+1]
    return (i+1) 

def quicksort(arr, start, end):
    if start<end:
        pivot= partition(arr, start, end)
        quicksort(arr, start, pivot-1)
        quicksort(arr, pivot+1, end)
f=open("text.txt","r")
height=f.readlines()
list=[]
for i in range(len(height)):
    list.append(height[i].rstrip('\n'))
quicksort(list, 0, len(height)-1)
f=open("text.txt","w")
for stud in list:
    f.write(stud)
    f.write("\n")
f.close()
print("File has been sorted")
