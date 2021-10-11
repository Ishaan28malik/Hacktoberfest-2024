import time
import random

weather = ["sunny", "rainy", "stormy", "windy", "snowy", "dark"]
ambience = random.choice(weather)
tools = ["flashlight", "stick", "bat", "gun", "phone", "knife"]
weapon = random.choice(tools)
emotions = ["scared", "tired", "nervous", "crying", "sweating"]
condition = random.choice(emotions)


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(0.2)


def intro():
    print_pause("You woke up from your nap.")
    print_pause("It's a " + ambience + " afternoon.")
    print_pause("You heard a strange noise coming from the backyard.")
    print_pause("The noise is getting more bolder and louder.")
    print_pause("You are so curious.\n")


def first_move():
    print_pause("You grab a " + weapon + " and head towards the back door.")
    print_pause("You sneak to the backdoor slowly and smoothly.")
    print_pause("As you get closer the noise seems so familiar.")
    print_pause("Would you run away?")
    choice = int(input('1.yes or 2.no \n'))
    if choice == 2:
        print_pause("It's the same wild Boar from yesterday.")
        print_pause("It stopped eating the sack of potatoes on the floor.")
        print_pause("It looked around and finally saw you.")
        print_pause("Both of you are staring.")
        print_pause("Initiate attack?")
        attack = int(input('1.yes or 2.no \n'))
        if attack == 1:
            print_pause("You lift up your hand with your " +
                        weapon + " and smash it on the wall.")
            print_pause("The boar run away as quickly as it can.")
        if attack == 2:
            print_pause("The boar growl and roar. Trying to scare you.")
            print_pause("As you lift your hand, it run away quickly.")
        conclusion()
    elif choice == 1:
        print_pause("You run fast heading back and close the door.")
        conclusion()
    else:
        print_pause("You're a warrior.\n")
        conclusion()


def second_move():
    print_pause("You grab your keys and lock the back door.")
    print_pause("You called someone and told them to come and get you.")
    print_pause("You were " + condition + " and waiting for help to come.")
    print_pause("The noise suddenly stop.")
    print_pause("You calm down and went out of bed.")
    print_pause("Would you like to continue? ")
    next_step = int(input('1.yes or 2.no \n'))
    if next_step == 1:
        print_pause("You went slowy heading to the backdoor.")
        print_pause("Your dog suddenly appeared behind you.")
        print_pause("That surprises you and felt relief.")
        conclusion()
    elif next_step == 2:
        print_pause("You stayed in bed and went back to sleep.")
        conclusion()
    else:
        print_pause("Would you like to continue? 1. continue or 2. no \n")
        conclusion()


def reaction():
    print_pause("Enter 1 to go out and investigate.")
    print_pause("Enter 2 to lock the door and call for help.")
    print_pause("What will you do?")
    moves = int(input("(Please enter 1 or 2)\n"))
    if moves == 1:
        first_move()
    elif moves == 2:
        second_move()
    else:
        conclusion()


def conclusion():
    print_pause("Would you like to restart?\n")
    play_again = int(input("(Please enter 1.yes or 2.no)\n"))
    if play_again == 1:
        print_pause("Okay, mighty warrior.")
        reaction()
    elif play_again == 2:
        print_pause("You're a brave warrior.")
    else:
        print_pause("Please enter 1 or 2")
        conclusion()


def play_game():
    intro()
    reaction()


play_game()
