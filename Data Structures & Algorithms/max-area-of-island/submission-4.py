class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # we will use dfs with four directions
        # the thing is we have to find all islands 
        # once we find an island, we will need to find the area of that island(how many 1)
        # then we just keep track of a global max to get the answer
        # Time O(m*n)
        # Space O(m*n) due to the recursion stack
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(row, col) -> int: # return area of the island
            nonlocal dirs
            area = 1 # current area
            grid[row][col] = 0 # mark as visited by flipping to water
            for d in dirs:
                new_row = row + d[0]
                new_col = col + d[1]
                if (new_row < 0 or new_row >= len(grid)) or (new_col < 0 or new_col >= len(grid[0])):
                    continue # out of bound
                if grid[new_row][new_col] == 1:
                    area  += dfs(new_row, new_col) # current area + next land area
            return area

        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    area = dfs(row, col)
                    max_area = max(max_area, area)
        return max_area