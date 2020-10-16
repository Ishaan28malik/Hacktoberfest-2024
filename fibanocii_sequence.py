def fib(n):
    if (n<=1):
        return n
    else:
        return fib((n)-1)+fib((n)-2)
n = int(input("enter number:"))
if n<=0:
    print("enter positive integer")
for i in range(n):
    print(fib(i))