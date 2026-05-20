class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # each step we have 8 moves and 4 general directions 
        # top right;          top left        bottom right     bottom left
        dirs = [[2,1], [1,2], [-2,1], [-1,2], [2,-1], [1,-2],  [-2,-1], [-1,-2]]
        # min steps to reach the target?
        # can we use recursion to track all paths that can reach the target?
        # not good, because the board is infinite and the knight can move in cycles forever. 
        # Recursive DFS would explore tons of paths and may never naturally know which path is minimum
        # When every move has the same cost, and we want the minimum number of moves, think BFS, not DFS/backtracking
        # this make sense as say at the same level, whichever path you go have the same cost
        # the min number of moves is bascially the level number which you can reach the target!
        # Time: O(number of visited positions before reaching target)
        # Space: O(number of visited positions)
        q = deque()
        q.append((0,0))
        visited = set()
        visited = {(0, 0)}
        level = 0
        # board is symmetrical
        # so we fix the answer at quadrant 1
        x = abs(x)
        y = abs(y)
        while q:
            qLen = len(q)
            for _ in range(qLen):
                r, c = q.popleft()
                
                if r == x and c == y:
                    return level
                for dx, dy in dirs:
                    newR = r + dx
                    newC = c + dy
                    if (newR, newC) in  visited or newR < -5 or newC < -5: # answer is in quadrant 1, but we allow to go outside of the q1 a bit,
                        continue
                    q.append((newR, newC))
                    visited.add((newR,newC))
                
            level += 1
        return level