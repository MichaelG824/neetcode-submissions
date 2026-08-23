class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        def capture(r, c):
            if (r < 0 or c < 0 or r == ROWS or
                c == COLS or board[r][c] != "O"
            ):
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)
        
        for i in range(len(board)):
            if board[i][0] == 'O':
                capture(i, 0)
            if board[i][-1] == 'O':
                capture(i, COLS - 1)
        
        for j in range(len(board[0])):
            if board[0][j] == 'O':
                capture(0, j)
            if board[-1][j] == 'O':
                capture(ROWS - 1, j)


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'T':
                    board[i][j] = 'O'