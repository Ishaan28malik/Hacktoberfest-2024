'''Jumbled Word Game development'''

import random

def choose():
    words=['rainbow','computer','laptop','hardware','software','umbrella','internet']
    pick=random.choice(words)
    return pick

def jumble(word):
    jumbled=" ".join(random.sample(word,len(word)))
    return jumbled

def thank(p1n,p2n,pp1,pp2):
    print( "Congratulations !!!", p1n," your final score is: ",pp1, end='\n\n')
    print( "Congratulations !!!", p2n," your final score is: ",pp2, end='\n\n')
    print("Thanks for playing")

def play():
    p1name=input("Player 1, Please enter your name. ")
    p2name=input("Player 2, Please enter your name. ")

    pp1=0  #scores of two players are initially at zero.
    pp2=0
    turn=0  #turn starts from zero and gradually increases on even and odd turns.

    while(1):
        picked_word=choose()
        qn=jumble(picked_word)
        print("The jumbled word is:", qn)  #Question preparation

        if(turn%2==0):
            print(p1name, " Its your turn.")
            ans=input("Can you tell the exact right word?  ")

            if(ans==picked_word):
                pp1=pp1+1
                print("Your score is now: ", pp1, end='\n\n')
            else:
                print("Sorry wrong answer, Better luck next time. The correct word would be: ", picked_word, end='\n')

            c=int(input("Press 1 to continue the game, and 0 to end the game     "))
            if(c==0):
                thank(p1name,p2name,pp1,pp2)
                break
        else:
            print(p2name, " Its your turn.")
            ans=input("Can you tell the exact right word?  ")

            if(ans==picked_word):
                pp2=pp2+1
                print("Your score is now: ", pp2, end='\n\n')
            else:
                print("Sorry wrong answer, Better luck next time. The correct word would be: ", picked_word, end='\n')

            c=int(input("Press 1 to continue the game, and 0 to end the game     "))
            if(c==0):
                thank(p1name,p2name,pp1,pp2)
                break

        turn=turn+1


play()
