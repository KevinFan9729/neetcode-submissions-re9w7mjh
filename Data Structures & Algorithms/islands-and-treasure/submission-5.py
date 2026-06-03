class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # we will be starting from the chest location
        # then we will do bfs
        # we do bfs as the min distance from chest to land is the level
        # Time O(m*n)
        # Space O(m*n)
        ROW, COL = len(grid), len(grid[0])
        q = deque()
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append((r,c)) # get all the chest location first
        
        level = 1
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        while q:
            qLen = len(q)
            for _ in range(qLen):
                r,c = q.popleft()
                for dx, dy in dirs:
                    newR = r + dx
                    newC = c + dy
                    if newR < 0  or newR >= ROW or newC < 0  or newC >= COL:
                        continue # out of bound!
                    if grid[newR][newC] == -1:
                        continue # cannot go into water
                    if grid[newR][newC] == 2147483647:
                        # this is an land that we can reach at this level!
                        grid[newR][newC] = level
                        q.append((newR, newC))
            level += 1