term = int(input("Enter Terms: "))

# variable initialization
first = 0
second = 1
count = 0

#condition for integer input
if term <= 0:
    print("Positive Integers Only.")
else:
    while count < term:
        print(first)
        fib = first + second
        first = second
        second = fib
        count += 1
