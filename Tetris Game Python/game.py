#!/usr/bin/python

"""
Python implementation of text-mode version of the Tetris game

Quick play instructions:

 - a (return): move piece left
 - d (return): move piece right
 - w (return): rotate piece counter clockwise
 - s (return): rotate piece clockwise
 - e (return): just move the piece downwards as is

"""

import os
import random
import sys

from copy import deepcopy

# DECLARE ALL THE CONSTANTS
BOARD_SIZE = 20
# Extra two are for the walls, playing area will have size as BOARD_SIZE
EFF_BOARD_SIZE = BOARD_SIZE + 2

PIECES = [

    [[1], [1], [1], [1]],

    [[1, 0],
     [1, 0],
     [1, 1]],

    [[0, 1],
     [0, 1],
     [1, 1]],

    [[0, 1],
     [1, 1],
     [1, 0]],

    [[1, 1],
     [1, 1]]

]

# Constants for user input
MOVE_LEFT = 'a'
MOVE_RIGHT = 'd'
ROTATE_ANTICLOCKWISE = 'w'
ROTATE_CLOCKWISE = 's'
NO_MOVE = 'e'
QUIT_GAME = 'q'

def print_board(board, curr_piece, piece_pos, error_message=''):
    """
    Parameters:
    -----------
    board - matrix of the size of the board
    curr_piece - matrix for the piece active in the game
    piece_pos - [x,y] co-ordinates of the top-left cell in the piece matrix
                w.r.t. the board

    Details:
    --------
    Prints out the board, piece and playing instructions to STDOUT
    If there are any error messages then prints them to STDOUT as well
    """
    os.system('cls' if os.name=='nt' else 'clear')
    print("Text mode version of the TETRIS game\n\n")

    board_copy = deepcopy(board)
    curr_piece_size_x = len(curr_piece)
    curr_piece_size_y = len(curr_piece[0])
    for i in range(curr_piece_size_x):
        for j in range(curr_piece_size_y):
            board_copy[piece_pos[0]+i][piece_pos[1]+j] = curr_piece[i][j] | board[piece_pos[0]+i][piece_pos[1]+j]

    # Print the board to STDOUT
    for i in range(EFF_BOARD_SIZE):
        for j in range(EFF_BOARD_SIZE):
            if board_copy[i][j] == 1:
                print("*", end='')
            else:
                print(" ", end='')
        print("")

    print("Quick play instructions:\n")
    print(" - a (return): move piece left")
    print(" - d (return): move piece right")
    print(" - w (return): rotate piece counter clockwise")
    print(" - s (return): rotate piece clockwise")

    # In case user doesn't want to alter the position of the piece
    # and he doesn't want to rotate the piece either and just wants to move
    # in the downward direction, he can choose 'f'
    print(" - e (return): just move the piece downwards as is")
    print(" - q (return): to quit the game anytime")

    if error_message:
        print(error_message)
    print("Your move:",)


def init_board():
    """
    Parameters:
    -----------
    None

    Returns:
    --------
    board - the matrix with the walls of the gameplay
    """
    board = [[0 for x in range(EFF_BOARD_SIZE)] for y in range(EFF_BOARD_SIZE)]
    for i in range(EFF_BOARD_SIZE):
        board[i][0] = 1
    for i in range(EFF_BOARD_SIZE):
        board[EFF_BOARD_SIZE-1][i] = 1
    for i in range(EFF_BOARD_SIZE):
        board[i][EFF_BOARD_SIZE-1] = 1
    return board


def get_random_piece():
    """
    Parameters:
    -----------
    None

    Returns:
    --------
    piece - a random piece from the PIECES constant declared above
    """
    idx = random.randrange(len(PIECES))
    return PIECES[idx]


def get_random_position(curr_piece):
    """
    Parameters:
    -----------
    curr_piece - piece which is alive in the game at the moment

    Returns:
    --------
    piece_pos - a randomly (along x-axis) chosen position for this piece
    """
    curr_piece_size = len(curr_piece)

    # This x refers to rows, rows go along y-axis
    x = 0
    # This y refers to columns, columns go along x-axis
    y = random.randrange(1, EFF_BOARD_SIZE-curr_piece_size)
    return [x, y]


def is_game_over(board, curr_piece, piece_pos):
    """
    Parameters:
    -----------
    board - matrix of the size of the board
    curr_piece - matrix for the piece active in the game
    piece_pos - [x,y] co-ordinates of the top-left cell in the piece matrix
                w.r.t. the board
    Returns:
    --------
    True - if game is over
    False - if game is live and player can still move
    """
    # If the piece cannot move down and the position is still the first row
    # of the board then the game has ended
    if not can_move_down(board, curr_piece, piece_pos) and piece_pos[0] == 0:
        return True
    return False


def get_left_move(piece_pos):
    """
    Parameters:
    -----------
    piece_pos - position of piece on the board

    Returns:
    --------
    piece_pos - new position of the piece shifted to the left
    """
    # Shift the piece left by 1 unit
    new_piece_pos = [piece_pos[0], piece_pos[1] - 1]
    return new_piece_pos


def get_right_move(piece_pos):
    """
    Parameters:
    -----------
    piece_pos - position of piece on the board

    Returns:
    --------
    piece_pos - new position of the piece shifted to the right
    """
    # Shift the piece right by 1 unit
    new_piece_pos = [piece_pos[0], piece_pos[1] + 1]
    return new_piece_pos


def get_down_move(piece_pos):
    """
    Parameters:
    -----------
    piece_pos - position of piece on the board

    Returns:
    --------
    piece_pos - new position of the piece shifted downward
    """
    # Shift the piece down by 1 unit
    new_piece_pos = [piece_pos[0] + 1, piece_pos[1]]
    return new_piece_pos


def rotate_clockwise(piece):
    """
    Paramertes:
    -----------
    piece - matrix of the piece to rotate

    Returns:
    --------
    piece - Clockwise rotated piece

    Details:
    --------
    We first reverse all the sub lists and then zip all the sublists
    This will give us a clockwise rotated matrix
    """
    piece_copy = deepcopy(piece)
    reverse_piece = piece_copy[::-1]
    return list(list(elem) for elem in zip(*reverse_piece))


def rotate_anticlockwise(piece):
    """
    Paramertes:
    -----------
    piece - matrix of the piece to rotate

    Returns:
    --------
    Anti-clockwise rotated piece

    Details:
    --------
    If we rotate any piece in clockwise direction for 3 times, we would eventually
    get the piece rotated in anti clockwise direction
    """
    piece_copy = deepcopy(piece)
    # Rotating clockwise thrice will be same as rotating anticlockwise :)
    piece_1 = rotate_clockwise(piece_copy)
    piece_2 = rotate_clockwise(piece_1)
    return rotate_clockwise(piece_2)


def merge_board_and_piece(board, curr_piece, piece_pos):
    """
    Parameters:
    -----------
    board - matrix of the size of the board
    curr_piece - matrix for the piece active in the game
    piece_pos - [x,y] co-ordinates of the top-left cell in the piece matrix
                w.r.t. the board

    Returns:
    --------
    None

    Details:
    --------
    Fixes the position of the passed piece at piece_pos in the board
    This means that the new piece will now come into the play

    We also remove any filled up rows from the board to continue the gameplay
    as it happends in a tetris game
    """
    curr_piece_size_x = len(curr_piece)
    curr_piece_size_y = len(curr_piece[0])
    for i in range(curr_piece_size_x):
        for j in range(curr_piece_size_y):
            board[piece_pos[0]+i][piece_pos[1]+j] = curr_piece[i][j] | board[piece_pos[0]+i][piece_pos[1]+j]

    # After merging the board and piece
    # If there are rows which are completely filled then remove those rows

    # Declare empty row to add later
    empty_row = [0]*EFF_BOARD_SIZE
    empty_row[0] = 1
    empty_row[EFF_BOARD_SIZE-1] = 1

    # Declare a constant row that is completely filled
    filled_row = [1]*EFF_BOARD_SIZE

    # Count the total filled rows in the board
    filled_rows = 0
    for row in board:
        if row == filled_row:
            filled_rows += 1

    # The last row is always a filled row because it is the boundary
    # So decrease the count for that one
    filled_rows -= 1

    for i in range(filled_rows):
        board.remove(filled_row)

    # Add extra empty rows on the top of the board to compensate for deleted rows
    for i in range(filled_rows):
        board.insert(0, empty_row)


def overlap_check(board, curr_piece, piece_pos):
    """
    Parameters:
    -----------
    board - matrix of the size of the board
    curr_piece - matrix for the piece active in the game
    piece_pos - [x,y] co-ordinates of the top-left cell in the piece matrix
                w.r.t. the board

    Returns:
    --------
    True - if piece do not overlap with any other piece or walls
    False - if piece overlaps with any other piece or board walls
    """
    curr_piece_size_x = len(curr_piece)
    curr_piece_size_y = len(curr_piece[0])
    for i in range(curr_piece_size_x):
        for j in range(curr_piece_size_y):
            if board[piece_pos[0]+i][piece_pos[1]+j] == 1 and curr_piece[i][j] == 1:
                return False
    return True


def can_move_left(board, curr_piece, piece_pos):
    """
    Parameters:
    -----------
    board - matrix of the size of the board
    curr_piece - matrix for the piece active in the game
    piece_pos - [x,y] co-ordinates of the top-left cell in the piece matrix
                w.r.t. the board

    Returns:
    --------
    True - if we can move the piece left
    False - if we cannot move the piece to the left,
            means it will overlap if we move it to the left
    """
    piece_pos = get_left_move(piece_pos)
    return overlap_check(board, curr_piece, piece_pos)


def can_move_right(board, curr_piece, piece_pos):
    """
    Parameters:
    -----------
    board - matrix of the size of the board
    curr_piece - matrix for the piece active in the game
    piece_pos - [x,y] co-ordinates of the top-left cell in the piece matrix
                w.r.t. the board

    Returns:
    --------
    True - if we can move the piece left
    False - if we cannot move the piece to the right,
            means it will overlap if we move it to the right
    """
    piece_pos = get_right_move(piece_pos)
    return overlap_check(board, curr_piece, piece_pos)


def can_move_down(board, curr_piece, piece_pos):
    """
    Parameters:
    -----------
    board - matrix of the size of the board
    curr_piece - matrix for the piece active in the game
    piece_pos - [x,y] co-ordinates of the top-left cell in the piece matrix
                w.r.t. the board

    Returns:
    --------
    True - if we can move the piece downwards
    False - if we cannot move the piece to the downward direction
    """
    piece_pos = get_down_move(piece_pos)
    return overlap_check(board, curr_piece, piece_pos)


def can_rotate_anticlockwise(board, curr_piece, piece_pos):
    """
    Parameters:
    -----------
    board - matrix of the size of the board
    curr_piece - matrix for the piece active in the game
    piece_pos - [x,y] co-ordinates of the top-left cell in the piece matrix
                w.r.t. the board

    Returns:
    --------
    True - if we can move the piece anti-clockwise
    False - if we cannot move the piece to anti-clockwise
            might happen in case rotating would overlap with any existing piece
    """
    curr_piece = rotate_anticlockwise(curr_piece)
    return overlap_check(board, curr_piece, piece_pos)


def can_rotate_clockwise(board, curr_piece, piece_pos):
    """
    Parameters:
    -----------
    board - matrix of the size of the board
    curr_piece - matrix for the piece active in the game
    piece_pos - [x,y] co-ordinates of the top-left cell in the piece matrix
                w.r.t. the board

    Returns:
    --------
    True - if we can move the piece clockwise
    False - if we cannot move the piece to clockwise
            might happen in case rotating would overlap with any existing piece
    """
    curr_piece = rotate_clockwise(curr_piece)
    return overlap_check(board, curr_piece, piece_pos)


def play_game():

    """
    Parameters:
    -----------
    None

    Returns:
    --------
    None

    Details:
    --------
    - Initializes the game
    - Reads player move from the STDIN
    - Checks for the move validity
    - Continues the gameplay if valid move, else prints out error msg
      without changing the board
    - Fixes the piece position on board if it cannot be moved
    - Pops in new piece on top of the board
    - Quits if no valid moves and possible for a new piece
    - Quits in case user wants to quit

    """

    # Initialize the game board, piece and piece position
    board = init_board()
    curr_piece = get_random_piece()
    piece_pos = get_random_position(curr_piece)
    print_board(board, curr_piece, piece_pos)

    # Get player move from STDIN
    player_move = input()
    while (not is_game_over(board, curr_piece, piece_pos)):
        ERR_MSG = ""
        do_move_down = False
        if player_move == MOVE_LEFT:
            if can_move_left(board, curr_piece, piece_pos):
                piece_pos = get_left_move(piece_pos)
                do_move_down = True
            else:
                ERR_MSG = "Cannot move left!"
        elif player_move == MOVE_RIGHT:
            if can_move_right(board, curr_piece, piece_pos):
                piece_pos = get_right_move(piece_pos)
                do_move_down = True
            else:
                ERR_MSG = "Cannot move right!"
        elif player_move == ROTATE_ANTICLOCKWISE:
            if can_rotate_anticlockwise(board, curr_piece, piece_pos):
                curr_piece = rotate_anticlockwise(curr_piece)
                do_move_down = True
            else:
                ERR_MSG = "Cannot rotate anti-clockwise !"
        elif player_move == ROTATE_CLOCKWISE:
            if can_rotate_clockwise(board, curr_piece, piece_pos):
                curr_piece = rotate_clockwise(curr_piece)
                do_move_down = True
            else:
                ERR_MSG = "Cannot rotate clockwise!"
        elif player_move == NO_MOVE:
            do_move_down = True
        elif player_move == QUIT_GAME:
            print("Bye. Thank you for playing!")
            sys.exit(0)
        else:
            ERR_MSG = "That is not a valid move!"

        if do_move_down and can_move_down(board, curr_piece, piece_pos):
            piece_pos = get_down_move(piece_pos)

        # This means the current piece in the game cannot be moved
        # We have to fix this piece in the board and generate a new piece
        if not can_move_down(board, curr_piece, piece_pos):
            merge_board_and_piece(board, curr_piece, piece_pos)
            curr_piece = get_random_piece()
            piece_pos = get_random_position(curr_piece)

        # Redraw board
        print_board(board, curr_piece, piece_pos, error_message=ERR_MSG)

        # Get player move from STDIN
        player_move = input()

    print("GAME OVER!")

if __name__ == "__main__":
    play_game()
