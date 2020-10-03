import time
def searching(a,n,search):
    return _searching(a,0,n-1,search)
def _searching(a,first,last,search):
    if(first>last):
        return -1
    mid=(first+last)//2
    if search>a[mid]:
        return _searching(a,mid+1,last,search)
    elif search<a[mid]:
        return _searching(a,first,mid-1,search)
    else:
        return mid
    
n=int(input("Enter no. of elements="))
a=[None]*n
for i in range(n):
    a[i]=int(input("enter element="))
search=int(input("element to be searched="))
seconds=time.time()
pos=searching(a,n,search)
if pos==-1:
    print("element not found")
else:
    print("element present at",pos+1)
print("function execution time:",(time.time()-seconds))
