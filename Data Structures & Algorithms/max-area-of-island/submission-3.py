class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # we will use dfs with four directions
        # the thing is we have to find all islands 
        # once we find an island, we will need to find the area of that island(how many 1)
        # then we just keep track of a global max to get the answer
        # Time O(m*n)
        # Space O(m*n)
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = set()
        def dfs(row, col) -> int: # return area of the island
            nonlocal dirs, visited
            area = 1 # current area
            visited.add((row, col)) # add the current pos to visited
            for d in dirs:
                new_row = row + d[0]
                new_col = col + d[1]
                if (new_row < 0 or new_row >= len(grid)) or (new_col < 0 or new_col >= len(grid[0])):
                    continue # out of bound
                if grid[new_row][new_col] == 1 and ((new_row, new_col)) not in visited:
                    area  += dfs(new_row, new_col) # current area + next land area
            return area

        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and ((row, col)) not in visited:
                    area = dfs(row, col)
                    max_area = max(max_area, area)

        return max_area