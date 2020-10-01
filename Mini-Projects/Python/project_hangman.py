import random

def hangman():
    word = random.choice(["divyanshu", "cat", "dog", "classroom", "students", "hangman","strangers","christmas","house","cake","pastries"])
    valid_letters = "abcdefghijklmnopqrstuvwxyz"
    attempts = 10
    guess_made = ''                 #guess made by the user

    while len(word) > 0:            #to ensure that the random choice is not empty
        main = ""                   #store the previous letters entered by the user
        # missed = 0

        for letter in word:
            if letter in guess_made:
                main = main + letter
            else:
                main = main + "_" + " "
        
        if main == word:
            print(main)
            print("Wuhuu you won this game")
            break


        print("Guess the word", main)
        guess = input()
        
        if guess in valid_letters:
            guess_made = guess_made + guess
        else:
            print("Enter a valid character")
            guess = input()
        
        if guess not in word:
            attempts = attempts - 1
            if attempts == 9:
                print("Only 9 attempts left\n")
                print("--------------")
            if attempts == 8:
                print("Only 8 attempts left\n")
                print("--------------")
                print("      O       ")
            if attempts == 7:
                print("Only 7 attempts left\n")
                print("--------------")
                print("      O       ")
                print("      |       ")
            if attempts == 6:
                print("Only 6 attempts left\n")
                print("--------------")
                print("      O       ")
                print("      |       ")
                print("     /        ")
            if attempts == 5:
                print("Only 5 attempts left\n")
                print("--------------")
                print("      O       ")
                print("      |       ")
                print("     / \      ")
            if attempts == 4:
                print("Only 4 attempts left\n")
                print("--------------")
                print("    \ O       ")
                print("      |       ")
                print("     / \      ")
            if attempts == 3:
                print("Only 3 attempts left\n")
                print("--------------")
                print("    \ O /     ")
                print("      |       ")
                print("     / \      ")
            if attempts == 2:
                print("Only 2 attempts left\n")
                print("--------------")
                print("    \ O_|     ")
                print("      |       ")
                print("     / \      ")
            if attempts == 1:
                print("Only 1 attempts left\n")
                print("--------------")
                print("        |     ")
                print("    \ O_|     ")
                print("      |\      ")
                print("     / \      ")
            if attempts == 0:
                print("OOOHHHH Snapp")
                print("You lose the game")
                print("You are responsible for man's death")
                print("--------------")
                print("        |     ")
                print("      O_|     ")
                print("     /|\      ")
                print("     / \      ")
                break




user_name = input("Enter your name\n")
print("Welcome {}, get ready to play the awesome game".format(user_name) )
print("-------------------------------------------------------------------------------\n")
print("                             ---> HANGMAN GAME <--               ")
print(" ")
print(" ")
print("How to play: Try to guess the word in less than 10 attempts")
print("             If you will encounter the wrong letter you")
print("             will lose a chance from given 10 chances\n")
print("-------------------------------------------------------------------------------\n")
hangman()
                       



# Algorithm:
# -> develop the interface
# -> predefined list(list of words that have to be guessesd)
# -> Instruction (guess the user made, list of all valid letters)
# -> Check the words
#    if word is correct then enter in empty list then draw figure
# -> reduce the turns 
# -> generate the figure