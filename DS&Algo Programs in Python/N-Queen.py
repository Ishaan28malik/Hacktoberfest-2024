# The N-Queens problem is like a puzzle where you have N queens and a 
# chessboard, and you need to place the queens on the board so that they can't
# attack each other. The goal is to find all the ways to do this. It's a 
# challenging problem that requires careful thinking and strategy.

class NQueen:
    def __init__(self):
        pass

    # Check if it's safe to place a queen at a given position
    def check(self, board, row, col, n):
        # Check the left side of the current row
        for i in range(col):
            if board[row][i]:
                return False

        # Check the upper-left diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j]:
                return False

        # Check the lower-left diagonal
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j]:
                return False

        print(f"Placed queen q{col + 1} at row {row + 1}")
        return True

    # Solve the N-Queens problem using backtracking
    def solve_nqueens(self, board, col, n):
        if col >= n:
            print("-------------------------------------------------------------------------------------")
            print("ALL QUEENS ARE PLACED")
            print("-------------------------------------------------------------------------------------")
            return True

        for i in range(n):
            if self.check(board, i, col, n):
                board[i][col] = 1

                print("-------------------------------------------------------------------------------------")
                for row in board:
                    print("\t".join(["q" + str(row.index(1) + 1) if cell == 1 else "0" for cell in row]))
                print("-------------------------------------------------------------------------------------")

                if self.solve_nqueens(board, col + 1, n):
                    return True

                print("-------------------------------------------------------------------------------------")
                print(f"Backtrack queen q{col + 1}")
                print("-------------------------------------------------------------------------------------")

                board[i][col] = 0

        return False

if __name__ == "__main__":
    n_queen = NQueen()
    
    while True:
        n = int(input("Enter the chessboard size (size should be greater than 3): "))
        print("-------------------------------------------------------------------------------------")
        
        if n <= 3:
            print("Please enter a size greater than 3:")
            print("-------------------------------------------------------------------------------------")
        else:
            board = [[0 for _ in range(n)] for _ in range(n)]
            print("Initially the board is:")
            
            for row in board:
                print("\t".join(["0" for _ in range(n)]))
            
            print("-------------------------------------------------------------------------------------")
            n_queen.solve_nqueens(board, 0, n)
            print("-------------------------------------------------------------------------------------")
            print("AFTER PLACING THE QUEEN: ")
            
            for row in board:
                print("\t".join(["q" + str(row.index(1) + 1) if cell == 1 else "0" for cell in row]))
            
            print("-------------------------------------------------------------------------------------")
