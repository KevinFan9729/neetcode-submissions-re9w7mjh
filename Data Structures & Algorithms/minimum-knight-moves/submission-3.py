class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # we will use bfs
        # notice at every level, the cost is the same (the level)
        # so when bfs first reach the target pos, that level is the answer

        dirs = [[2,1],[1,2],[-1,2],[-2,1],[-2,-1],[-1,-2],[1,-2],[2,-1]]
        # notice that the board is symmetric so we can lock answer to the first q
        x = abs(x)
        y = abs(y)
        if x == 0  and y == 0:
            return 0
        q = deque()
        visited = set()
        q.append((0,0))
        level=0
        while q:
            qLen = len(q)
            for _ in range(qLen):
                r,c = q.popleft()
                for dx, dy in dirs:
                    newR = r + dx
                    newC = c + dy
                    if newR == x and newC == y:
                        return level + 1
                    if (newR, newC) in visited or newR < -5 or newC < -5: # answer is in first q
                        continue
                    q.append((newR,newC))
                    visited.add((newR,newC))
            level +=1