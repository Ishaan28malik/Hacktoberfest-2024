def mergetwo(x,y):
    sortlist = []
    sze = len(x) + len(y)

    l = 0
    r = 0
    for i in range(sze):
        if l>=len(x) or r>=len(y):
            break
        elif x[l]<=y[r]:
            sortlist.append(x[l])
            l+=1
        elif x[l]>y[r]:
            sortlist.append(y[r])
            r+=1
    if l<len(x):
        while(l!=len(x)):
            sortlist.append(x[l])
            l+=1
    elif r<len(y):
        while(r!=len(y)):
            sortlist.append(y[r])
            r+=1
    
    return sortlist

        



def mergesort(lst,start,end):
    if start==end:
        return [lst[start]]
    else:
        mid = (start+end)//2
        x  = mergesort(lst,start,mid)
        y = mergesort(lst,mid+1,end)
        
        return mergetwo(x,y)
        






n = int(input())
lst = list(map(int, input().split()))
print(mergesort(lst,0,n-1))






