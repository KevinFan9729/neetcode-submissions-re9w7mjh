class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # O(m*n)
        rows, cols = len(grid), len(grid[0])
        visited = set()
        maxArea = 0
        def findIslandAreaBFS(r,c):
            queue = deque()
            queue.append((r,c))
            visited.add((r,c))
            area = 1

            while queue:
                pos_x, pos_y = queue.popleft()
                dirs = [[0,1],[0,-1],[1,0],[-1,0]]
                for dx, dy in dirs:
                    move_x = pos_x+dx
                    move_y = pos_y+dy
                    if ((min(move_x, move_y)<0) or (move_x == rows or move_y == cols) or
                        ((move_x,move_y) in visited) or (grid[move_x][move_y]==0)):
                        continue # invalid cases, move on
                    area +=1
                    queue.append((move_x,move_y))
                    visited.add((move_x, move_y))
            return area

        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] == 1 and not((r,c) in visited)):  # found a new island!
                    islandArea = findIslandAreaBFS(r,c)
                    maxArea = max(maxArea, islandArea)
        return maxArea