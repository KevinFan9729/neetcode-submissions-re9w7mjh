class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # we need to find how many fresh fruit we have first
        # this is bfs
        # we need to collect the position of rotten fruits
        # then start from the rotten fruits and at each level,
        # we will turn fresh fruits into rotten
        # we keep track of level and that is our min minutes
            # if fresh fruit at the end is zero, otherwise; impossible
        # Time O(n*m)
        # Space O(n*m) # entire graph
        ROW, COL = len(grid), len(grid[0])

        q = deque()
        freshCount = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    freshCount += 1
                elif grid[r][c] == 2:
                    q.append((r,c)) # initial rotten pos
        if freshCount == 0 and len(q) == 0:
            # no rotten, no fresh
            return 0
        level = 0
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        while q and freshCount>0:
            qLen = len(q)
            for _ in range(qLen):
                r,c = q.popleft()
                for dx, dy in dirs:
                    newR = r + dx
                    newC = c + dy
                    if newR >= ROW or newC >= COL or newR < 0  or newC < 0:
                        continue
                    if grid[newR][newC] == 0 or grid[newR][newC] == 2:
                        continue
                    # the only left case is where grid[newR][newC] == 1
                    freshCount-=1
                    grid[newR][newC] = 2 # mark as rotten
                    q.append((newR, newC))
            level += 1
        return level if freshCount == 0 else -1