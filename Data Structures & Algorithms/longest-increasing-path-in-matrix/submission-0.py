class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # can we do recursively?
        # use dfs?
        # to make sure you are strictly increasing, we need to check if the next number is greater than the 
        # current when we are trying to navigate.
        # if we can navigate, then the count for the sequence is plus one!
        # base case?
            # if we are out of bound, return 0
        # O(m*n * 4^(m*n)) in time
        # O(m+n) in space
        rows, cols = len(matrix), len(matrix[0])
        def dfs(r,c):
            sequence_len = -1
            dirs = [[0,1],[0,-1],[1,0],[-1,0]]
            for dx, dy in dirs:
                move_x, move_y = r + dx, c + dy
                if ((min(move_x,move_y)<0 or (move_x == rows or move_y == cols) or 
                matrix[r][c]>= matrix[move_x][move_y])):
                    continue # direction will not work 
                # consider all driections and see which path is the longest
                sequence_len = max(sequence_len, dfs(move_x, move_y) + 1)
            if sequence_len == -1:
                return 1
            return sequence_len
        
        max_len = float('-inf')
        # O(m*n) here 
        for r in range(rows):
            for c in range(cols):
                length = dfs(r,c)
                max_len = max(max_len, length)
        return max_len