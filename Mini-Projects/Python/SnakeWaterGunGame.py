# Snake Water Gun Game Devlopement
import random
NoOfRound = 10
user = 0
comp = 0

while NoOfRound > 0:
    print("---------------------------------")
    print("Choices:\nS-Snake\nW-Water\nG-Gun")
    c = input("Enter Your Choice:-")
    choice = c.capitalize()

    if choice in ('S', 'W', 'G'):

        n = random.randint(1, 3)

        if (choice == 'S' and n == 1) or (choice == 'W' and n == 2) or (choice == 'G' and n == 3):
            print("Draw")

        elif choice == "S":
            if n == 2:
                print("Congratulations. You Won!")
                user += 1
            else:
                print("Better Luck Next Time!")
                comp += 1

        elif choice == "W":
            if n == 3:
                print("Congratulations. You Won!")
                user += 1
            else:
                print("Better Luck Next Time!")
                comp += 1

        else:
            if n == 1:
                print("Congratulations. You Won!")
                user += 1
            else:
                print("Better Luck Next Time!")
                comp += 1

    else:
        print("Invalid Choice")
        continue
    NoOfRound -= 1

print("---------------------------------")

if user == comp:
    print("Draw!")
elif user > comp:
    print("Hurray. You won!")
else:
    print("You Lost!")

print("---------------------------------")

print("Scoreboard")
print("Your Score:-", user, "\nComputer's Score:-", comp )

print("---------------------------------")








