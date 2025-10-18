"""
Start Script, choose the options you want play and start, 
play until you want exit (exit by !exit)

Stores your score in results.txt file

Enter your name: > Tim
Hello, Tim
> rock,gun,lightning,devil,dragon,water,air,paper,sponge,wolf,tree,human,snake,scissors,fire
Okay, let's start
> rock
Sorry, but computer chose air
> !rating
Your rating: 0
> rock
Well done. Computer chose sponge and failed
> !rating
Your rating: 100
> !exit
Bye!


"""

import random

all_options = ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air',
               'paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire']

game_mode = True

double_all_options = all_options * 2
all_losing_options = {}
for key in range(len(all_options)):
    all_losing_options[all_options[key]] = double_all_options[key + 1:key + 8]


player = str(input("Enter Your name: "))
print("Hello, " + player)

file = open("rating.txt", "r")
data = file.read()
data = [plr.split(" ") for plr in data]
score = 0

for plr in data:
    if plr[0] == player:
        score = plr[1]
        break
file.close()

user_choose = str(input());
if user_choose == "":
    values = ["rock", "paper", "scissors"]
else:
    values = user_choose.split(",")

active_options = {}
for key in all_losing_options:
    if key in values:
        temp = []
        for op in all_losing_options[key]:
            if op in values:
                temp.append(op)
        active_options[key] = temp

print("Okay, let's start")


def save_in_txt():
    file_to_save = open("rating.txt", "w")
    data_write = file_to_save.read()
    data_write = [plr.split(" ") for plr in data_write]
    for plr in data_write:
        if plr[0] == player:
            plr[1] = score
            break
    file_to_save.writelines([players[0] + " " + players[1] for players in data])


while game_mode:
    try:
        system_choice = values[random.randrange(len(values))]
        user_choice = str(input())
        if user_choice == system_choice:
            score += 50
            print("There is a draw " + system_choice)
        elif user_choice == "!exit":
            game_mode = False
            print("Bye!")
            break
        elif user_choice == "!rating":
            print("Your rating: ", score)
        elif system_choice in active_options[user_choice] :
            print("Sorry, but computer chose " + system_choice)
        elif user_choice in active_options[system_choice] :
            score += 100
            print("Well done. Computer chose " + system_choice + " and failed")
    except KeyError:
        print("Invalid input")