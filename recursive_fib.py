def fib(n):
	if(n==0):
		return 0
	if(n==1):
		return 1
	else:
		return fib(n-1)+fib(n-2)

n=int(input("Enter the number of elements in Fibonacci series: "))
print("Fibonacci series containing ",n,"elements is: ")

for i in range(n):
	print(fib(i),end=" ")
print("\n")