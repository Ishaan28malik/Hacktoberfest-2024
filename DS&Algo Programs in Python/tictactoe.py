sample = [[1,2,3],[4,5,6],[7,8,9]]

ar = [['','',''],
      ['','',''],
      ['','','']]

def tictactoe():
    print('Welcome to the TicTacToe game!')
    print('In order to make your moves, please follow the positional map below:')
    print_game(sample)
    player = 'x'
    while(1):
        print(player, "'s turn")
        user_input = input('Provide move:')
        move = int(user_input)
        playMove(move, player)
        print_game(ar)

        if win(ar) == True:
            print(player, ' wins the game!')
            break
        if draw(ar) == True:
            print('Game ended in a draw!')
            break
            
        if player == 'x':
            player = 'o'
        else:
            player = 'x'

def playMove(move, player):
    if move > 0 and move <= 9:
            if move == 1:
                if ar[0][0] == '':
                    ar[0][0] = player
            elif move == 2:
                if ar[0][1] == '':
                    ar[0][1] = player
            elif move == 3:
                if ar[0][2] == '':
                    ar[0][2] = player
            elif move == 4:
                if ar[1][0] == '':
                    ar[1][0] = player
            elif move == 5:
                if ar[1][1] == '':
                    ar[1][1] = player
            elif move == 6:
                if ar[1][2] == '':
                    ar[1][2] = player
            elif move == 7:
                if ar[2][0] == '':
                    ar[2][0] = player
            elif move == 8:
                if ar[2][1] == '':
                    ar[2][1] = player
            elif move == 9:
                if ar[2][2] == '':
                    ar[2][2] = player

def win(ar):
    if ar[0][0] == ar[0][1] == ar[0][2] == 'x' \
       or ar[1][0] == ar[1][1] == ar[1][2] == 'x' \
       or ar[2][0] == ar[2][1] == ar[2][2] == 'x':
        return True

    if ar[0][0] == ar[1][0] == ar[2][0] == 'x' \
       or ar[0][1] == ar[1][1] == ar[2][1] == 'x' \
       or ar[0][2] == ar[1][2] == ar[2][2] == 'x':
        return True

    if ar[0][0] == ar[1][1] == ar[2][2] == 'x' \
       or ar[2][0] == ar[1][1] == ar[0][2] == 'x':
        return True
    
    if ar[0][0] == ar[0][1] == ar[0][2] == 'o' \
       or ar[1][0] == ar[1][1] == ar[1][2] == 'o' \
       or ar[2][0] == ar[2][1] == ar[2][2] == 'o':
        return True

    if ar[0][0] == ar[1][0] == ar[2][0] == 'o' \
       or ar[0][1] == ar[1][1] == ar[2][1] == 'o' \
       or ar[0][2] == ar[1][2] == ar[2][2] == 'o':
        return True

    if ar[0][0] == ar[1][1] == ar[2][2] == 'o' \
       or ar[2][0] == ar[1][1] == ar[0][2] == 'o':
        return True

    return False

def draw(ar):
    for i in ar:
        for j in i:
            if j == '':
                return False
    return True

def print_game(ar):
    for i in ar:
        print(i)
        
tictactoe()
