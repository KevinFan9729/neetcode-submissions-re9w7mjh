class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # ok finding the perimter is not as simple as 
        # counting how many `lands`
        # their sides needs to be removed in the final cal
        # if they are connected
        # a sqaure can lose all its sides in the cal if its fully inside
        # can lose 1-3 as well
        # hmmmm...
        # once we find a land +4 to the result, check neigbor
        # if a neigbor is found, -1
        # Time O(n*m)
        # Space O(n*m) due to the visited set

        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        ans = 0
        max_r = len(grid)
        max_c = len(grid[0])
        visited = set()
        def dfs(row, col):
            nonlocal dirs, ans, max_r, max_c
            # add the current island 4 sides
            ans+=4
            visited.add((row,col))
            for d in dirs:
                new_r = row + d[0]
                new_c = col + d[1]
                if ((new_r < 0 or new_r >= max_r) or 
                    (new_c < 0  or new_c >= max_c)):
                    # we are out of range, this index pair is not valid
                    continue 
                if grid[new_r][new_c] == 0:
                    # water encountered
                    continue
                if grid[new_r][new_c] == 1:
                    ans-=1
                    if (new_r, new_c) not in visited:
                        dfs(new_r, new_c)



        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # we found the one and only island
                # as the qeustion stated there is only 1 isaland
                if grid[row][col] == 1:
                    dfs(row, col)
                    # once we are done terversing this island, 
                    # we have the result
                    return ans
