class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # we must loop through the matrix first to see where are zeros
        # make a helper function to loop through the row to turn the row to all zero
        # make a helper function to loop through the column to turn the col to all zero
        rows, cols = len(matrix), len(matrix[0])

        def turnRowZero(row):
            for i in range(cols):
                matrix[row][i] = 0
        
        def trunColZero(col):
            for i in range(rows):
                matrix[i][col] = 0

        zeroPos = []
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zeroPos.append([r,c])
        
        while zeroPos:
            zero_row, zero_col = zeroPos.pop()
            turnRowZero(zero_row)
            trunColZero(zero_col)