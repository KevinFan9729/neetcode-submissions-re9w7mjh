class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # we will loop through the board to find the starting position of "O"
            # if an "O" is found 
                # use dfs to navigate the entire island
                # while navigating, check if any the region of "O" is touching
                # the board boundary
                    # if it is touching, record a boolen flag to not to capture this region but we mark the entire region as visisted so we will not search in the same region again
                    # if the region is not touching the board boundary, good we can loop through the region and turn all position inside of that region to "X" i.e. capture
        
        # each cell is visisted once
        # O(m*n) in time 
        # O(m*n) in space
        rows, cols = len(board), len(board[0])
        def dfs(r,c):
            nonlocal captureFlag
            visited.add((r,c))
            region.add((r,c))
            if (r == 0 or r == rows-1) or (c == 0 or c == cols-1):
                captureFlag = False 
            dirs = [[0,1],[0,-1],[1,0],[-1,0]]
            for dx, dy in dirs:
                move_x, move_y = r+dx, c+dy
                if(min(move_x, move_y)<0 or (move_x == rows or move_y == cols) or (move_x, move_y) in visited
                or board[move_x][move_y] == "X"):
                    continue
                dfs(move_x, move_y)
        
        def capture(region):
            while region:
                posX, posY = region.pop()
                board[posX][posY] = "X"
        
        visited = set()
        for r in range(rows):
            for c in range(cols):
                captureFlag = True
                region = set()
                if (r,c) not in visited and board[r][c] == "O":
                    dfs(r,c)
                    if captureFlag:
                        capture(region)