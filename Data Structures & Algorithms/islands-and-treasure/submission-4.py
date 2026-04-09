class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # we can start from the treasure chest position
        # and do bfs on all starting treasure points!

        rows, cols = len(grid), len(grid[0])
        q = deque()
        # we will find all chest first
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        level = 1
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        while q:
            qLen = len(q)
            for i in range(qLen):
                r, c = q.popleft()
                for dx, dy in dirs:
                    moveX, moveY = r+dx, c+dy
                    if (min(moveX, moveY)<0 or
                    (moveX == rows or moveY == cols) or
                    grid[moveX][moveY]!=2147483647):
                        continue
                    grid[moveX][moveY] = min(grid[moveX][moveY], level)
                    q.append((moveX, moveY))
            level +=1

        
