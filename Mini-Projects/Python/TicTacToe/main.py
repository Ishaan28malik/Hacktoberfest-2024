player1 = ""
player2 = ""

def welcome():
    print("Welcome to Tic Tac Toe!")
    print("Choose your symbol ('X' or 'O') -- ")
    print("***********************************")
    
    while True:
        global player1
        global player2
        player1 = input("Player 1 : ").upper()
        if player1 == "X":
            player2 =  "O"
        elif player1 == "O":
            player2 = "X"
        else:
            print("Warning! Please choose only 'X' or 'O'")
            continue
        break
    print("")
    print("")
    print(f"Player1 chooses {player1}")
    print(f"Player2 chooses {player2}")
    print("")
    print("***INSTRUCTIONS****")
    print("")
    print("EXAMPLE BOARD")
    print("7 | 8 | 9")
    print("----------")
    print("4 | 5 | 6")
    print("----------")
    print("1 | 2 | 3")
    print("")

def playBoard(position):
    print("")
    print(f"{position[7-1]} | {position[8-1]} | {position[9-1]}")
    print("----------")
    print(f"{position[4-1]} | {position[5-1]} | {position[6-1]}")
    print("----------")
    print(f"{position[1-1]} | {position[2-1]} | {position[3-1]}")
    print("")

def play():
    position = ['','','','','','','','','']
    global player1
    global player2
    winner = ""
    while winner=="":
        while winner=="":
            playBoard(position)
            choice1 = int(input("Player1's turn-- choose your place: "))
            if position[choice1-1] == '':
                position[choice1-1] = player1
                if (
                     position[0] == position[4] == position[8] == player1 or 
                     position[6] == position[4] == position[2] == player1 or
                     position[6] == position[3] == position[0] == player1 or
                     position[7] == position[4] == position[1] == player1 or
                     position[8] == position[5] == position[2] == player1 or
                     position[6] == position[7] == position[8] == player1 or
                     position[3] == position[4] == position[5] == player1 or
                     position[0] == position[1] == position[2] == player1 
                   ):
                   winner="player1"
                   break
                elif (
                        position[0] != '' and position[1] != '' and position[2] != '' and
                        position[3] != '' and position[4] != '' and position[5] != '' and
                        position[6] != '' and position[7] != '' and position[8] != ''
                     ):
                    winner="draw"
                    break
                break
            else:
                print("")
                print("WARNING! THE PLACE IS ALREADY TAKEN, Please try again.")
                print("")
                
        while winner=="":
            playBoard(position)
            choice2 = int(input("Player2's turn-- choose your place: "))
            if position[choice2-1] == '':
                position[choice2-1] = player2
                if (
                     position[0] == position[4] == position[8] == player2 or 
                     position[6] == position[4] == position[2] == player2 or
                     position[6] == position[3] == position[0] == player2 or
                     position[7] == position[4] == position[1] == player2 or
                     position[8] == position[5] == position[2] == player2 or
                     position[6] == position[7] == position[8] == player2 or
                     position[3] == position[4] == position[5] == player2 or
                     position[0] == position[1] == position[2] == player2 
                   ):
                   winner="player2"
                elif (
                        position[0] != '' and position[1] != '' and position[2] != '' and
                        position[3] != '' and position[4] != '' and position[5] != '' and
                        position[6] != '' and position[7] != '' and position[8] != ''
                     ):
                    winner="draw"
                    break
                break
            else:
                print("")
                print("WARNING! THE PLACE IS ALREADY TAKEN, Please try again.")
                print("")
    playBoard(position)

    if winner == "draw":
        print("********************")
        print("Match DRAW!")
        print("********************")

    else:
        print("========================")
        #print("************************")
        print("OUR WINNER IS: "+winner)
        #print("************************")
        print("========================")
                



welcome()
play()
