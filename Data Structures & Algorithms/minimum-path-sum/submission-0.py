class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # so we have 2 choices at each steps
        # down or right
        # at any stop we do not care how we get there
        # but we do care what is the minium cost to reach that spot
        ROWS, COLS = len(grid), len(grid[0])
        memo = {}
        def dfs(r, c):
            if r == ROWS -1 and c == COLS - 1:
                # we are now reaching the final pos
                return grid[r][c]
            if r >= ROWS or c >= COLS:
                return float('inf') # invalid path
            if (r,c) in memo:
                return memo[(r,c)]
            # down or right
            downR = r + 1
            rightC = c +1
            goDown = dfs(downR, c)
            goRight = dfs(r, rightC)
            currMinCost = grid[r][c] + min(goDown, goRight)
            memo[(r,c)] = currMinCost
            return currMinCost
        res = dfs(0,0)
        return res