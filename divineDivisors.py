N = int(input())
arr = []
for i in range(1,N+1):  #get the divisors of number
    if N % i == 0:
        
        arr.append(i)
sorted(arr) #printing in ascending order
print(arr)
