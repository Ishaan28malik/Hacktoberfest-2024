import numpy as np
grid = [[0, 0, 0, 2, 6, 0, 7, 0, 1],
        [6, 8, 0, 0, 7, 0, 0, 9, 0],
        [1, 9, 0, 0, 0, 4, 5, 0, 0],
        [8, 2, 0, 1, 0, 0, 0, 4, 0],
        [0, 0, 4, 6, 0, 2, 9, 0, 0],
        [0, 5, 0, 0, 0, 3, 0, 2, 8],
        [0, 0, 9, 3, 0, 0, 0, 7, 4],
        [0, 4, 0, 0, 5, 0, 0, 3, 6],
        [7, 0, 3, 0, 1, 8, 0, 0, 0]]


def it_can(x, y, n):
    global grid
    for i in range(9):
        if(grid[x][i] == n or grid[i][y] == n):
            return False
    x_ = (x//3)*3
    y_ = (y//3)*3
    for i in range(3):
        for j in range(3):
            if(grid[x_+i][y_+j] == n):
                return False
    return True


def solve():
    global grid
    for i in range(9):
        for j in range(9):
            if(grid[i][j] == 0):
                for n in range(1, 10):
                    if(it_can(i, j, n) == True):
                        grid[i][j] = n
                        solve()
                        grid[i][j] = 0
                return

    print(np.matrix(grid))
    input("more solutions ?")


solve()
