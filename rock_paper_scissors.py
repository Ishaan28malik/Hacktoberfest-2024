import random

n=int(input("Enter the winning score: "))
pl1=0
com=0
while(pl1<n and com<n):
    p=input("Pick one from Rock, Paper and Scissor: ")
    str=p.lower()
    c=random.choice(["rock","paper","scissor"])
    if(str=="rock"):
        if(c=="rock"):
            print("Computer chose ",c,". It's a Tie!")
            print("\nScore:\nYou: ",pl1,"\nComputer: ",com)
        elif(c=="paper"):
            print("Computer chose ",c,". Computer Wins!")
            com+=1
            print("\nScore:\nYou: ",pl1,"\nComputer: ",com)
        else:
            print("Computer chose ",c,". You win!")
            pl1+=1
            print("\nScore:\nYou: ",pl1,"\nComputer: ",com)
    
    elif(str=="paper"):
        if(c=="rock"):
            print("Computer chose ",c,". You Win!")
            pl1+=1
            print("\nScore:\nYou: ",pl1,"\nComputer: ",com)
        elif(c=="paper"):
            print("Computer chose ",c,". It's a Tie!")
            print("\nScore:\nYou: ",pl1,"\nComputer: ",com)
        else:
            print("Computer chose ",c,". Computer Wins!")
            com+=1
            print("\nScore:\nYou: ",pl1,"\nComputer: ",com)
    elif(str=="scissor"):
        if(c=="rock"):
            print("Computer chose ",c,". Computer Wins!")
            com+=1
            print("\nScore:\nYou: ",pl1,"\nComputer: ",com)
        elif(c=="paper"):
            print("Computer chose ",c,". You Win!")
            pl1+=1
            print("\nScore:\nYou: ",pl1,"\nComputer: ",com)
        else:
            print("Computer chose ",c,". It's a Tie!")
            print("\nScore:\nYou: ",pl1,"\nComputer: ",com)
    else:
        print("Please enter a correct option.")

print("\nFinal score:\nYou: ",pl1,"\nComputer: ",com)
if(pl1>com):
    print("YOU WIN!")
elif(pl1<com):
    print("COMPUTER WINS!")
else:
    print("IT'S A TIE!")
