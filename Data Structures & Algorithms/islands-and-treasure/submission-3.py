class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # BFS from the target!
        # O(m*n)
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        visted = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c)) # add all treasure first, Note all treasure will be at the SAME level
                    visted.add((r,c))
        length = 0
        while queue:
            queue_len = len(queue)
            for _ in range(queue_len):
                pos_x, pos_y = queue.popleft()
                grid[pos_x][pos_y] = length
                dirs = [[1,0],[-1,0],[0,1],[0,-1]]
                for dx, dy in dirs:
                    move_x = pos_x+ dx
                    move_y = pos_y +dy
                    if (min(move_x,move_y)<0 or 
                        (move_x==rows or move_y == cols) or
                        ((move_x,move_y) in visted) or (grid[move_x][move_y] == -1)):
                        continue
                    queue.append((move_x,move_y))
                    visted.add((move_x,move_y))
            length += 1