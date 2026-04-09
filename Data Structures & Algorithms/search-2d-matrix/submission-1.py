class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # we can use dfs to solve this question
        # we will visit each cell to see if a number can be found
        # O(m*n) time bceuase of the visited set, each cell will only be visited once
        # O(m*n) space bceuase of the visited set
        visited = set()
        def dfs(r,c):
            rows, cols = len(matrix), len(matrix[0])
            if matrix[r][c] == target:
                return True
            visited.add((r,c))
            dirs = [[0,1],[0,-1],[1,0]]
            for dx, dy in dirs:
                move_x = r + dx
                move_y = c + dy
                if (min(move_x, move_y)<0 or (move_x == rows or move_y == cols) or
                (move_x,move_y) in visited):
                    continue
                if dfs(move_x, move_y):
                    return True
            return False
        ans = dfs(0,0)
        return ans                