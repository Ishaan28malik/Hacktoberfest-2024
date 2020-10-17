def bappi(i,a,n):
    j=cn=0
    for j in range(i+1,n):
        if(a[i]<a[j]):
            cn=cn+1
    return cn
def hi(n,a):
    # Document it for future use
    i=0
    for j in range(2*n):
        cn=bappi(i,a,n)
        print(cn)
        if(cn==0):
            #print(a)
            i=i+1
        if(i==n):
            #print(a)
            break
        else:
            #print(a)
            a[i],a[i+cn]=a[i+cn],a[i]
            print(a)
a=input().rstrip().split()
for i in range(len(a)):
    a[i]=int(a[i])
hi(len(a),a)
print(a[::-1])

# Document it for future use
