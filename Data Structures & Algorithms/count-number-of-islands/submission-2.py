from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # O(m*n)
        visited = set()
        island_count = 0
        rows, cols = len(grid), len(grid[0])
        # row go down, column: horizontal move

        def dfs(r,c):
            # exclude all invalid cases
            if (min(r,c)<0) or (r==rows or c == cols) or (r,c) in visited or grid[r][c] == "0":
                return
            visited.add((r,c))
            dirs = [[0,1], [0,-1], [1,0], [-1,0]]
            for dx, dy in dirs:
                dfs(r+dx, c+dy)
        # def dfs2(r,c):
        #     # include all valid cases
        #     if (min(r,c)>=0) and (r!=rows and c != cols) and not((r,c) in visited) and grid[r][c] == "1":
        #         visited.add((r,c))
        #         dirs = [[0,1], [0,-1], [1,0], [-1,0]]
        #         for dx, dy in dirs:
        #             dfs2(r+dx, c+dy)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    island_count += 1
                    dfs(r, c)

        return island_count
        