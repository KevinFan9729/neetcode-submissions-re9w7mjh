class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # we have two choices at each steps
        # move down or move right 
        # recursion dfs(row, col) -> num of unique path to reach the end
        # start is 0,0, end is m-1, n-1
        # Time O(m*n)
        # Space O(m*n)

        memo = {}
        def dfs(row, col):
            if row == m-1 and col == n-1:
                return 1
            if (row, col) in memo:
                return memo[(row, col)]
            # right is [0,1]
            # down is [1,0]
            dirs = [[0,1],[1,0]]

            path = 0
            for d in dirs:
                newRow = row + d[0]
                newCol = col + d[1]
                if newRow >=m or newCol >=n: # out of bound
                    continue
                path += dfs(newRow, newCol)
            memo[(row, col)] = path
            return path

        res = dfs(0,0)
        return res