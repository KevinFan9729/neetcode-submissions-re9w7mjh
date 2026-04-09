class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # BFS to find 0? and repeatly run on all avaiable slots
        # O(m*n)^2
        rows, cols = len(grid), len(grid[0])

        def BFSfindShortestPath(r,c):
            queue = deque()
            visted = set()
            queue.append((r,c))
            visted.add((r,c))
            length = 0

            while queue:
                queue_len = len(queue)
                for _ in range(queue_len):
                    pos_x, pos_y = queue.popleft()
                    if grid[pos_x][pos_y] == 0:
                        return length
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
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2147483647:
                    grid[r][c] = BFSfindShortestPath(r,c)