class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # We will loop through the boundary "O" first and mark those region as cannot be captured
        # each cell is visisted once
        # O(m*n) in time 
        # O(1) in space
        rows, cols = len(board), len(board[0])
        def dfs(r,c):
            board[r][c] = "T" # mark as cannot be captured
            dirs = [[0,1],[0,-1],[1,0],[-1,0]]
            for dx, dy in dirs:
                move_x, move_y = r+dx, c+dy
                if(min(move_x, move_y)<0 or (move_x == rows or move_y == cols) or board[move_x][move_y] != "O"):
                    continue
                dfs(move_x, move_y)
        for c in range(cols):
            if board[0][c] == "O":
                dfs(0,c)
            if board[rows-1][c] == "O":
                dfs(rows-1,c)

        for r in range(rows):
            if board[r][0] == "O":
                dfs(r,0)
            if board[r][cols-1] == "O":
                dfs(r,cols-1)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X" # capture
                if board[r][c] == "T":
                    board[r][c] = "O"
                    