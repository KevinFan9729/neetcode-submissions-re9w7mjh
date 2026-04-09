class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows, cols = m, n
        # O(2^(m+n)) in time as we can go to two directions at each step
        # O(m*n) in space this is the space of the call stack
        def dfs(r,c):
            if ((r<0) or (r == rows or c == cols)):
                return 0
            if (r == rows-1 and c == cols -1):
                return 1
            count = 0
            dirs = [[0,1],[1,0]]# two possible directions, right and down
            for dx, dy in dirs:
                move_x, move_y = r+dx, c+dy
                count += dfs(move_x, move_y)
            return count
        ans = dfs(0,0)
        return ans

        