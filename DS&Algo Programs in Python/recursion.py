def fib(n):
  if (n==1 or n==2):
    return 1
  else:
    return fib(n-1)+fib(n-2)#recursion step
print(fib(5))#printing 5th elemnet in fibonacci series using recursion
