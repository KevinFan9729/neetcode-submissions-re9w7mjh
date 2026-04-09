class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows , cols = len(board), len(board[0])

        def dfs(r, c, index):
            if ((min(r,c) < 0) or (r == rows or c == cols) or ((r,c) in visited) or
                (board[r][c] != word[index])):
                return False
            
            if index ==  len(word)-1:
                return True
            # Mark the cell as visited by modifying the board
            # temp = board[r][c]
            visited.add((r,c))
            # board[r][c] = "#"
            
            dirs = [[0,1], [1,0], [0, -1], [-1,0]]
            for dx, dy in dirs:
                if dfs(r+dx, c+dy, index + 1):
                    return True
            
            # Unmark the cell (backtracking)
            # board[r][c] = temp
            # visited.remove((r,c))
            return False
        
        
        first_target_char = word[0]
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == first_target_char:
                    visited = set()
                    if dfs(r,c,0):
                        return True
        return False
