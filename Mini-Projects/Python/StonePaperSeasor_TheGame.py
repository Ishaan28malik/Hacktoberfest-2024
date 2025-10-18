import random

print("==============Ston Paper Seasor=============\n")

lis = ["Stone","Paper","Seasor"]

name = input("Enter yout name : \t")

print("I am SHIVAM. Lets play...")

comp = 0
me = 0

print("Enter 'st' for stone \t Enter 'p' for paper \t Enter 'se' for seasor \t Enter 'e' for end this game \n")


a = 1
while a==1 :
    co = random.choice(lis)
    n = input()

    if n == "e":
        break
    
    print("I gussed ",co)
    
    
    if n == "p" :
        if co == "Stone" :
            me = me + 1
            print ("You win \n")
            print ("Your points =", me)
            print ("My points =", comp)
            print ("\n")

        elif co == "Seasor":
            comp = comp + 1
            print ("You loss \n")
            print ("Your points =", me)
            print ("My points =", comp)
            print ("\n")

        elif co == "Paper" :
            print ("Draw \n")
            print ("Your points =", me)
            print ("My points =", comp)
            print ("\n")

    elif n == "st" :
        if co == "Seasor" :
            me = me + 1
            print ("You win \n")
            print ("Your points =", me)
            print ("My points =", comp)
            print ("\n")

        elif co == "Paper":
            comp = comp + 1
            print ("You loss \n")
            print ("Your points =", me)
            print ("My points =", comp)
            print ("\n")

        elif co == "Stone" :
            print ("Draw \n")
            print ("Your points =", me)
            print ("My points =", comp)
            print ("\n")

    elif n == "se" :
        if co == "Paper" :
            me = me + 1
            print ("You win \n")
            print ("Your points =", me)
            print ("My points =", comp)
            print ("\n")

        elif co == "Stone":
            comp = comp + 1
            print ("You loss \n")
            print ("Your points =", me)
            print ("My points =", comp)
            print ("\n")

        elif co == "Seasor" :
            print ("Draw \n")
            print ("Your points =", me)
            print ("My points =", comp)
            print ("\n")

    else :
        print("invalid syntex")


print ("\n")
print ("\n")
print ("\n")
print ("-----Game over----- \n")
print ("Your total points :   \t" , me)
print ("My total points : \t" , comp)
