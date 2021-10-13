##Based on the Collatz Conjecture
### The answer will always be 1

def weirdAlgorithm():
    x = int(input("Write a positive integer: "))
    process = str(x) + "-> "
    while x != 1 and x>0:
        if x%2 == 0:
            x = int(x/2)
            process += (str(x) +" -> ")
        else:
            x = x*3 + 1
            process += (str(x) + " -> ")
    process += ("Success")
    print(process)

weirdAlgorithm()