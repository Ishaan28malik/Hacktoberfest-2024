#-------------------------------------------#
#         BINARY SEARCH FUNCTION            #
#-------------------------------------------#


def binSearch(l,key):
    low  = 0
    high = len(l)
    mid  = 0

    while low < high:
        mid = (low+high)//2
        if l[mid] == key:
            return mid
        elif l[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return -1                        # if not found return -1


l = []                                  # list of Array that insert number
number = int(input("Enter a Number: "))
for i in range(number):
    l.append(int(input('Enter Next Number:  ')))

l.sort()                                # sort list
print(l)
key = int(input("Enter Key Element:     "))

if binSearch(l,Key) == -1:
    print("Element not Found \n")
else:
    print('KEY element Found At Location:   ',binSearch(l,key))
