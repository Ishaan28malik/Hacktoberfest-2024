#! /usr/bin/env python3

#This is a hangman game.
import random
wordList = 'Awkward Bagpipes Banjo Bungler Croquet Crypt Dwarves Fervid Fishhook Fjord Gazebo Gypsy Haiku Haphazard Hyphen Ivory Jazzy Jiffy Jinx Jukebox Kayak Kiosk Klutz Memento Mystify Numbskull Ostracize Oxygen Pajama Phlegm Pixel Polka Quad Quip Rhythmic Rogue Sphinx Squawk Swivel Toady Twelfth Unzip Waxy Wildebeest Yacht Zealous Zigzag Zippy Zombie'.lower().split()
HANGMAN_PICS = ['''
          
          
          
          
           ''','''
     
         
         
         
        ===''','''
     
         |
         |
         |
        ===''', '''
     +---+
         |
         |
         |
        ===''','''
     +---+
     O   |
         |
         |
        ===''', '''
     +---+
     O   |
     |   |
         |
        ===''', '''
     +---+
     O   |
    /|   |
         |
        ===''', '''
     +---+
     O   |
    /|\  |
         |
        ===''', '''
     +---+
     O   |
    /|\  |
    /    |
        ===''', '''
     +---+
     O   |
    /|\  |
    / \  |
        ===''']

def Main():
    while (True):
        intErr = 0
        gameOver = False
        print ("Welcome to Hangman.")
        print ("Now randomly selecting a word...")
        randWord = getRandomWord(wordList)
        randWordList = list(randWord)
        randWordHidden = ["_" for i in range (len(randWordList))]
        while (True):
            while (True):
                print (str(randWordHidden).replace("'","").replace("[","").replace("]","").replace(",",""))
                strGuess = input("What is your guess? \n").lower()
                if (strGuess not in "abcdefghijklmnopqrstuvwxyz" or len(strGuess) != 1):
                    print ("Please enter a single letter.")
                else:
                    break
            if (strGuess not in randWord):
                intErr +=1
                print ("You guessed wrong. You have " + str(len(HANGMAN_PICS)-1-intErr) + " incorrect guesses left.")
                print (getHangmanPic(intErr))
                if (intErr >= len(HANGMAN_PICS)-1):
                    print ("You ran out of guesses and were hung.")
                    gameOver = True
                    print ("The word was: " + randWord)
            else:
                print (strGuess + " is in the word.")
                for i in range (len(randWordList)):
                    if (randWordList[i] == strGuess):
                        randWordHidden[i] = strGuess
                if randWordHidden == randWordList:
                    gameOver = True
                    print (str(randWordHidden).replace("'","").replace("[","").replace("]","").replace(",",""))
                    print ("You won!")
                
            if (gameOver):
                break
        x = input ("Enter y to play again. Enter any other key to quit.")
        if (x.lower() != 'y'):
            break

def getRandomWord(words):
    randint = random.randint(0,len(words))
    return words[randint]

def getHangmanPic(intErrors):
    return HANGMAN_PICS[intErrors]
    
Main()
