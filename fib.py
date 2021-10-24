term = int(input("Enter Terms: "))
first = 0
second = 1
count = 0
if term <= 0:
    print("Positive Integers Only.")
else:
    while count < term:
        print(first)
        
        fib = first + second
        
        first = second
        second = fib
        
        count += 1

 def fib():
     n = int(input())
     a = 0
     b = 1
     p = []
     for i in range(n):
         p.append(a)
         a,b = b,a+b
     print(p)
fib()       
