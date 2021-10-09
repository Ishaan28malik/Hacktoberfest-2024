n = int(input("Enter a number: "))
if(n%2!=0):
    n=n+1
for i in range(2, n/2):
    if(n/2==0):
        f=0
        break
    else:
        f=1
if(f==1):
    print("Prime")
else:
    print("Not Prime")
