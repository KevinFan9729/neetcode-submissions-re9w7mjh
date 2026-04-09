class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # use graph treversal to navigate through all cells in the island
        # O(m*n) in time, at most each cell is visited once
        # O(1) in space
        rows, cols = len(grid), len(grid[0])
        def dfs(r,c):
            dirs = [[0,1],[0,-1],[1,0],[-1,0]]
            grid[r][c] = "0" # marked as visited
            for dx, dy in dirs:
                moveX = r + dx
                moveY = c + dy
                if (min(moveX, moveY)<0 or (moveX == rows or moveY == cols)
                or grid[moveX][moveY] == "0"):
                    continue
                dfs(moveX, moveY)
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count+=1
                    dfs(r,c)
        return count
