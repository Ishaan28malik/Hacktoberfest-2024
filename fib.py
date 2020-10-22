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
