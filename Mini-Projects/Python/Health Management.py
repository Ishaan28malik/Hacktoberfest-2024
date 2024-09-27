# Health Management System
# 3 clients - Gaurav, Hitesh and Hritik
# Total 6 files
# write a function that when executed takes as input client name
import datetime

def getdate():
    num = datetime.datetime.now()
    return num

def display():
    print("Press\n 1 for diet list\n 2 for exercise list")
    list_t = int(input("Enter your Choice: "))
    if (list_t == 1):
        with open(f"{name}.txt") as op:
            for i in op:
                print(i, end="")
    elif (list_t == 2):
        with open(f"{name}-ex.txt") as op:
            for i in op:
                print(i, end="")
    else:
        print("Invalid Choice")

def get():
    print(f"Welcome {name}\n\n")
    print("Press\n 1 to lock Diet\n 2 to lock Exercise\n 3 to open list\n")
    n = int(input("Enter choice: "))
    if (n == 1):
        while True:
            print("Enter what you have taken and in what time\n")
            value = input("Type here\n")
            with open(f"{name}.txt", "a") as op:
                op.write(str([str(getdate())]) + ":" + value + "\n")
            print("Successfully done")
            choice1 = input("Press Y to continue adding and N to exit: ")
            if (choice1 == "Y"):
                continue
            elif (choice1 == "N"):
                print("Your Details have been saved Successfully")
                break
            else:
                print("Invalid Choice")
                choice1 = input("Press Y to continue adding or N to exit: ")
                continue
    elif (n == 2):
        while True:
            print("Enter your exercise name:\n")
            value = input("Type here\n")
            with open(f"{name}-ex.txt", "a") as op:
                op.write(str([str(getdate())]) + ":" + value + "\n")
            print("Successfully done")
            choice1 = input("Press Y to continue adding and N to exit: ")
            if (choice1 == "Y"):
                continue
            elif (choice1 == "N"):
                print("Your Details have been saved Successfully")
                break
            else:
                print("Invalid Choice")
                choice1 = input("Press Y to continue adding or N to exit: ")
                continue

print("Welcome to our Health Management System !!! ")
print("\n")
# print("\n")
# print("\n")

print("Press\n 1 To Register New User\n2 To Show the List of User\n3 To Display Details of User\n4 To Enter Details Of User")
choice = int(input("Enter Choice: "))
if(choice == 1):
    while True:
        name = input("\nEnter the name of user: ")
        with open("names.txt", "a") as op:
            op.write(str([str(getdate())]) + ":" + name + "\n")
        print("Successfully done")
        choice1 = input("Press Y to continue adding and N to exit: ")
        if (choice1 == "Y"):
            continue
        elif (choice1 == "N"):
            print("Your Details have been saved Successfully")
            break
        else:
            print("Invalid Choice")
            choice1 = input("Press Y to continue adding or N to exit: ")
            continue
elif(choice == 2):
    with open("names.txt") as op:
        for i in op:
            print(i, end="")
elif(choice == 3):
    display()
elif(choice == 4):
    get()
else:
    print("Wrong choice")



