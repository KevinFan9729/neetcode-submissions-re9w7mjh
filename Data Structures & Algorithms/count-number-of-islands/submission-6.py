class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # use graph treversal to navigate through all cells in the island
        # O(m*n) in time, at most each cell is visited once
        # O(m*n) in space at most we visit all cells, so the hashset has all position!
        visited = set()
        rows, cols = len(grid), len(grid[0])
        def dfs(r,c):
            dirs = [[0,1],[0,-1],[1,0],[-1,0]]
            visited.add((r,c))
            for dx, dy in dirs:
                moveX = r + dx
                moveY = c + dy
                if (min(moveX, moveY)<0 or (moveX == rows or moveY == cols) or
                (moveX, moveY)in visited or grid[moveX][moveY] == "0"):
                    continue
                dfs(moveX, moveY)
        count = 0
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == "1":
                    count+=1
                    dfs(r,c)
        return count
