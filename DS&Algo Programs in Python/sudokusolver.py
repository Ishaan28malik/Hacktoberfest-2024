class Solution(object):
    def solveSudoku(self, board):
        def depthFsearch(cells, squ, rows, columns, board):
            if not cells:
                return True
            i, j = cells[-1]
            for num in range(0, 9):
                if rows[i][num] == columns[j][num] == squ[3 * (i / 3) + j / 3][num] == 0:
                    rows[i][num] = columns[j][num] = squ[3 * (i / 3) + j / 3][num] = 1
                    board[i][j] = str(num + 1)
                    if depthFsearch(cells[:-1], squ, rows, columns, board):
                        return True
                    board[i][j] = "."
                    rows[i][num] = columns[j][num] = squ[3 * (i / 3) + j / 3][num] = 0
            return False
        
        squ = [[0] * 9 for _ in range(9)]
        rows = [[0] * 9 for _ in range(9)]
        columns = [[0] * 9 for _ in range(9)]
        cells = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    cells.append((i, j))
                else:
                    num = int(board[i][j]) - 1
                    rows[i][num] = columns[j][num] = squ[3 * (i / 3) + j / 3][num] = 1
        depthFsearch(cells, squ, rows, columns, board)