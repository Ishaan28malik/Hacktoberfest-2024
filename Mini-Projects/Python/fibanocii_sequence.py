terms = int(input("Enter Terms: "))

first = 0
second = 1

count = 0

if terms <= 0:
    print("Positive Integers Only.")
else:
    while count < terms:
        print(first)
        
        nth = first + second
        
        first = second
        second = nth
        
        count += 1
