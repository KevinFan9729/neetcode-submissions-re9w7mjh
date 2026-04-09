from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs? looks like level order?
        # how about we start at rotton fruits first then do bfs
        # O(m*n)
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        visisted = set()
        # first collect all the position of the rotten fruit first
        count_one = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    count_one +=1
                if grid[r][c] == 2:
                    queue.append((r,c))
                    visisted.add((r,c))
        if count_one == 0: # no fresh fruit, need 0 time
            return 0
        time = -1
        while queue:
            queueLen = len(queue)
            for _ in range(queueLen):
                pos_x, pos_y = queue.popleft()
                dirs = [[0,1],[0,-1],[1,0],[-1,0]]
                for dx, dy in dirs:
                    move_x = pos_x + dx
                    move_y = pos_y + dy
                    if (min(move_x,move_y)<0 or (move_x == rows or move_y == cols) or # excluding factors
                    ((move_x,move_y) in visisted) or (grid[move_x][move_y] != 1)):
                        continue
                    count_one -= 1
                    queue.append((move_x,move_y))
                    visisted.add((move_x,move_y))
            time+=1

        if (count_one > 0): # still have fresh fruit in the grid after the rotting process
            return -1
        
        return time