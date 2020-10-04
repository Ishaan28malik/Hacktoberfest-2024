n=int(input("Enter a no:"))
a=0
b=1
print(a)
sum=a+b
print(sum)
for i in range(n):
    c=a+b
    a=b
    b=c
    print(c)
