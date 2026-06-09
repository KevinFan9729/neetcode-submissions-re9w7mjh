class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # once we find an piece of land, we will use graph trversal to mark all those lands as visited
        # Time O(n*m)
        # Space O(n*m)
        ROW, COL = len(grid), len(grid[0])
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        visited = set()
        def dfs(r,c):
            visited.add((r,c))

            for dx, dy in dirs:
                newR = r + dx
                newC = c + dy
                if newR <0 or newR >= ROW or newC < 0 or newC >= COL:
                    continue
                if (newR,newC) in visited:
                    continue
                if grid[newR][newC] == "1":
                    dfs(newR,newC)
        count = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1" and (r,c) not in visited:
                    count+=1
                    dfs(r,c)
        return count