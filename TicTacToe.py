import random

board = [" " for _ in range(9)]

def display_board(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("-----------")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("-----------")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])

def check_win(board, player):
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]

    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def check_draw(board):
    return " " not in board

def computer_move(board):
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if check_win(board, "O"):
                return i
            board[i] = " "

    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if check_win(board, "X"):
                return i
            board[i] = " "

    if board[4] == " ":
        return 4

    corners = [0, 2, 6, 8]
    random.shuffle(corners)
    for corner in corners:
        if board[corner] == " ":
            return corner

    sides = [1, 3, 5, 7]
    random.shuffle(sides)
    for side in sides:
        if board[side] == " ":
            return side

while True:
    display_board(board)

    while True:
        player_move = int(input("Enter your move (1-9): ")) - 1
        if player_move >= 0 and player_move < 9 and board[player_move] == " ":
            board[player_move] = "X"
            break
        else:
            print("Invalid move. Try again.")

    if check_win(board, "X"):
        display_board(board)
        print("You win! Congratulations!")
        break

    if check_draw(board):
        display_board(board)
        print("It's a draw!")
        break

    computer_move_index = computer_move(board)
    board[computer_move_index] = "O"

    if check_win(board, "O"):
        display_board(board)
        print("Computer wins! You lose!")
        break

    if check_draw(board):
        display_board(board)
        print("It's a draw!")
        break
