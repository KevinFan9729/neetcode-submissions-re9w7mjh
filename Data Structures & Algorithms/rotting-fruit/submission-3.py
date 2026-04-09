class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs go through level by level
        # start from the rotten ones 
        rows, cols = len(grid), len(grid[0])
        good_fruit_count = 0
        q = deque()
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    good_fruit_count+=1
                if grid[r][c] == 2:
                     q.append((r,c))
                     visited.add((r,c))
        if good_fruit_count == 0:
            return 0

        def bfs():
            nonlocal good_fruit_count
            time = -1
            dirs = [[0,1],[0,-1],[1,0],[-1,0]]
            while q:
                q_len = len(q)
                for _ in range(q_len):
                    r, c = q.popleft()
                    for dx, dy in dirs:
                        move_x = r + dx
                        move_y = c + dy
                        if ( (min(move_x,move_y) < 0) or 
                        (move_x == rows or move_y == cols) or 
                        (move_x,move_y) in visited or 
                        (grid[move_x][move_y] != 1)):
                            continue 
                        q.append((move_x,move_y))
                        visited.add((move_x,move_y))
                        good_fruit_count -= 1
                time+=1
            return time

        time = bfs()
        if good_fruit_count != 0:
            return -1
        return time
        

            
        