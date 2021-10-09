# Python program to demonstrate identity matix of entered number :

num = int(input("Enter a number : "))
for i in range(0, num):
    for j in range(0, num):
        if i == j:
            print("1", end="")
        else:
            print("0", end="")
    print("")