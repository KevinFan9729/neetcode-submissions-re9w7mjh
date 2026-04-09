from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # O(m*n)
        visited = set()
        island_count = 0
        rows, cols = len(grid), len(grid[0])
        # row go down, column: horizontal move

        def bfs(r,c):# this is used to mark all connected 1 that belongs to a particular island
            queue = deque()
            queue.append((r,c))
            visited.add((r,c))
            while queue:
                pos_x, pos_y = queue.popleft()
                # right, left, down, up
                dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dx, dy in dirs:
                    # if outside of the grid (top, left), or outside of grid (down, right) or already visited or hit water 
                    if (min(pos_x+dx, pos_y+dy) < 0) or (pos_x+dx == rows or pos_y+dy == cols) or ((pos_x+dx, pos_y+dy) in visited) or (grid[pos_x][pos_y] == "0"):
                        continue
                    queue.append((pos_x+dx, pos_y+dy))
                    visited.add((pos_x+dx, pos_y+dy))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    island_count += 1
                    bfs(r, c)

        return island_count
        