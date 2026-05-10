class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # find an island and then traverse the island and find area
        # keep track of a max area
        # Time O(m*n)
        # Space O(m*n)
        ROWS, COLS = len(grid), len(grid[0])
        def bfs(r,c):
            q= deque()
            q.append((r,c))
            visited.add((r,c))
            dirs = [[0,1],[0,-1],[1,0],[-1,0]]
            area = 1
            while q:
                currR, currC = q.popleft()
                for dx, dy in dirs:
                    newR = currR + dx
                    newC = currC + dy
                    if newR >= ROWS or newR < 0 or newC >= COLS or newC < 0:
                        # out of bound issue
                        continue
                    if grid[newR][newC] == 0 or (newR, newC) in visited:
                        # water or already visited
                        continue
                    area+=1
                    q.append((newR, newC))
                    visited.add((newR, newC))
            return area
        visited =set()
        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = bfs(r,c)
                    maxArea = max(maxArea, area)
        return maxArea  