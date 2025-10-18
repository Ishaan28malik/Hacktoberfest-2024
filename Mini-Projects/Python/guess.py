"""Guess a number within a range.
Exercises
1. Change the range to be from 0 to 1,000,000.
2. Can you still guess the number?
3. Print the number of guesses made.
4. Limit the number of guesses to the minimum required.
"""

from random import randint
from random import choice

start = 1
end = 100
value = randint(start, end)
flag=0
print("I'm thinking of a number between", start, "and", end)
guess = None

n=int(input("Enter number of players \n"))



while guess != value:
    turn=randint(1,n)
    print("Turn of player",turn)
    
    
    text = input("Guess the number: ")
    guess = int(text)
    

    luck= randint(1,10)
    #print(luck)
    if guess < value:
        print("Higher.")
    elif guess > value:
        print("Lower.")
    if luck==6:
        if value%2==0:
            print("even")
            flag=1
        else:
            print("Odd")
            flag=1
    if luck==7:
        print ("Number is close to:-->",value+randint(1,10))

print("Congratulations! You guessed the right answer:", value)

def bonus():
    mark=randint(1,2)
    if mark==1:
        print("points Wont be deducted")
    else:
        print("points will be deducted")
    point=input("Do you want to play the bonus question \n")
    ls=['a','e','i','o','u']
    hitormiss=choice(ls)
    if point=='y' or point=='yes':
        g2=input("Guess the vowel\n")
        if g2==hitormiss:
            print("Congratulations ! You Guessed the right vowel! ")
        else:
            print("Wrong ,the correct answer was (which you didnt get :p)",hitormiss)
    else:
        print("Disappointed from you.")

bonus()
