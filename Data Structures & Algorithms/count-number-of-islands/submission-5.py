class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # use dfs to cover the island once an island is found
        rows, cols = len(grid), len(grid[0])
        def dfs(r,c):
            visited.add((r,c)) # mark the island cell as visited
            dirs = [[1,0],[-1,0],[0,1],[0,-1]]
            for dx, dy in dirs:
                move_x = r + dx
                move_y = c + dy
                if((min(move_x, move_y)< 0) or (move_x == rows or move_y == cols) or
                (move_x, move_y) in visited or (grid[move_x][move_y] == "0")):
                    continue
                # visited.add((move_x, move_y)) # mark the island cell as visited
                dfs(move_x, move_y)
        
        count = 0
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    count += 1
                    dfs(r,c)
        return count
        