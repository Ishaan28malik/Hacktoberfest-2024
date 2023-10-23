# MONISHA MANDAL
# GITHUB - monishamandal02
# ADVENTURE GAME USING PYTHON

import time
import random


def print_pause(msg_to_print):
    print(msg_to_print)
    time.sleep(2)


def intro(item, anii):
    print_pause("You are standing in a field, filled "
                "with long trees and green grass.\n")
    print_pause("Everyone says that a " + anii + " is here, "
                " and has been terrifying the people of village.\n")
    print_pause("In front of you is a farm.\n")
    print_pause("To your right is a dense forest.\n")
    print_pause("In your hand you hold your trusty (but not very "
                "effective) knife.\n")


def fore(item, anii):
    if "sward" in item:
        print_pause("\nYou look with concentration.")
        print_pause("\nYou've been here before, and gotten all"
                    " It's just an noramal forest with trees and grass.")
        print_pause("\nYou came back to the field.\n")
    else:
        print_pause("\nYou peer cautiously into the cave.")
        print_pause("\nIt turns out to be only a very big forest.")
        print_pause("\nYour eye catches a glint of metal behind a "
                    "rock.")
        print_pause("\nYou have found the magical Sword of Ogoroth!")
        print_pause("\nYou throw your silly old knife and pick up "
                    "the sword with you.")
        print_pause("\nYou walk back out to the field.\n")
        item.append("sward")
    field(item, anii)


def farm(item, anii):
    print_pause("\nYou approach the door of the farm.")
    print_pause("\nYou are about to knock when the door "
                "opens and out steps a " + anii + ".")
    print_pause("\nEep! This is the " + anii + "'s house!")
    print_pause("\nThe " + anii + " attacks you!\n")
    if "sward" not in item:
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.\n")
    while True:
        choice2 = input("Would you like to (1) fight or (2) "
                        "run away?")
        if choice2 == "1":
            if "sward" in item:
                print_pause("\nAs the " + anii + " moves to attack, "
                            "you unsheath your new sword.")
                print_pause("\nThe Sword of Ogoroth shines brightly in "
                            "your hand as you brace yourself for the "
                            "attack.")
                print_pause("\nBut the " + anii + "takes one look at "
                            "your shiny new toy and runs away!")
                print_pause("\nYou have rid the town of the " + anii +
                            ". You are victorious!\n")
            else:
                print_pause("\nYou do your best...")
                print_pause("but your dagger is no match for the " + anii + ".")
                print_pause("\nYou have been defeated!\n")
            play_again()
            break
        if choice2 == "2":
            print_pause("\nYou run back into the field. "
                        "\nLuckily, you don't seem to have been "
                        "followed.\n")
            field(item, anii)
            break


def field(item, anii):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    while True:
        choice1 = input("(Please enter 1 or 2.)\n")
        if choice1 == "1":
            farm(item, anii)
            break
        elif choice1 == "2":
            fore(item, anii)
            break


def play_again():
    again = input("Would you like to play again? (y/n)").lower()
    if again == "y":
        print_pause("\n\n\nExcellent! Restarting the game ...\n\n\n")
        play_game()
    elif again == "n":
        print_pause("\n\n\nThanks for playing! See you next time.\n\n\n")
    else:
        play_again()


def play_game():
    item = []
    anii = random.choice(["way big", "foruarms", "dragon", "shenron"])
    intro(item, anii)
    field(item, anii)

if_name="adventure game"
play_game()