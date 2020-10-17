n=int(input("Enter a no:"))
a1=0
a2=1
print(a1)
sum = a1+a2
print(sum)
for i in range(0 , n):
    ai = a1 + a2
    a1 = a2
    a2 = ai
    print(ai)
