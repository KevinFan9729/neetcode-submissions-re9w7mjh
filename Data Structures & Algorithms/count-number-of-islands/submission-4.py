class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        def dfs(r,c):
            if ((min(r,c) <0) or 
            (r == rows or c ==cols) or 
            ((r,c) in visited) or 
            (grid[r][c]=="0")):
                return
            visited.add((r,c))
            dirs = [[0,1],[0,-1],[1,0],[-1,0]]
            for dx, dy in dirs:
                dfs(r+dx, c+dy)

        for r in range(rows):
            for c in range(cols):
            # new island!
                if (grid[r][c] == "1") and not((r,c) in visited):
                    num +=1
                    dfs(r,c) # mark all coordinates inside of this island as visited
            
        return num