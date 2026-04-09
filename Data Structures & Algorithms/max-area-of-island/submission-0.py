class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        maxArea = 0
        def findIslandAreaDFS(r,c):
            if ((min(r,c)<0) or (r==rows or c ==cols) or ((r,c) in visited) or (grid[r][c] == 0)):
                return 0
            visited.add((r,c))
            dirs = [[0,1],[0,-1],[1,0],[-1,0]]
            area = 1 # one valid cell has an area of 1
            for dx, dy in dirs:
                area += findIslandAreaDFS(r+dx, c+dy)
            return area

        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] == 1 and not((r,c) in visited)):
                    islandArea = findIslandAreaDFS(r,c)
                    maxArea = max(maxArea, islandArea)
        return maxArea