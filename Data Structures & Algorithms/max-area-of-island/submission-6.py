class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # once we found an island, the idea is we will find the area of this island
        # in the outerloop we can track the max island
        # Time O(n*m)
        # Space O(n*m)
        dirs = []
        visited = set()

        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        ROW, COL = len(grid), len(grid[0])


        def dfs(r,c):
            area = 1
            for dx, dy in dirs:
                newR = r + dx
                newC = c + dy
                if newR <0 or newR >= ROW or newC < 0 or newC >= COL:
                    continue
                if (newR, newC) in visited or grid[newR][newC] == 0:
                    continue
                visited.add((newR, newC))
                area += dfs(newR, newC)
            return area
        maxArea = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1 and (r,c) not in visited:
                    visited.add((r,c))
                    maxArea = max(maxArea, dfs(r,c))

        return maxArea