class NumMatrix:
    # prefix sum 2d

    def __init__(self, matrix: List[List[int]]):
        row, col = len(matrix), len(matrix[0])
        # we will pad zeros
        self.prefix_mat = [[0 for _ in range(col+1)] for _ in range(row+1)]
        for r in range(row):
            prefix = 0
            for c in range(col):
                prefix += matrix[r][c]
                above = self.prefix_mat[r][c+1]
                self.prefix_mat[r+1][c+1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottomRight = self.prefix_mat[row2+1][col2+1]
        aboveRight =  self.prefix_mat[row1][col2+1]
        bottomLeft = self.prefix_mat[row2+1][col1]
        topleft = self.prefix_mat[row1][col1]

        return bottomRight - aboveRight - bottomLeft + topleft
        
# let prefix[r][c] represent the sum of everything in the subrectangle from the top-left corner (0,0) to (r,c)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)