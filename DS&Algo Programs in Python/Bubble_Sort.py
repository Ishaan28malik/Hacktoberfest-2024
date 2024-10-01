# Python program to implement bubble sort

num = int(input("Enter a number : "))
list1 = [int(input("Ente an elements : ")) for i in range(num)]
print("Unsorted list : ", list1)

for i in range(len(list1)-1, 0, -1):
    
    for j in range(i):
        if list1[j] > list1[j+1]:
           list1[j], list1[j+1] = list1[j+1], list1[j]
           print(list1)
        else:
           print(list1)
           
    print()
		
print("Sorted List : ", list1)
		