class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # this is a graph treversal provblem
        # we use dfs with 4 directions
        # now once we find a NEW island (1) we start the treversal
        # the treversal will need to finda all lands in the island and mark them as visted
        # we then can count how many islands we have
        # Time O(m*n) we need to loop through all elements in the grid once
        # Space O(m*n) at worst, the visited set may be the same size as the grid (say all lands)

        visited = set()
        #up, down, left, right
        dirs = [[-1,0],[1,0],[0,-1],[0,1]]
        def dfs(row, col):
            nonlocal dirs, visited
            visited.add((row, col)) # mark current as visited
            for dir in dirs:
                new_row = row + dir[0]
                new_col = col + dir[1]
                if (new_row < 0 or new_row >= len(grid)) or (new_col < 0 or new_col >= len(grid[0])):
                    # out of bound check
                    continue
                if grid[new_row][new_col] == "1" and (new_row,new_col) not in visited:
                    dfs(new_row, new_col) # go to that land

        island_count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in visited:
                    # we found a new island that is not visted yet !
                    dfs(row, col)
                    island_count+=1
        return island_count
