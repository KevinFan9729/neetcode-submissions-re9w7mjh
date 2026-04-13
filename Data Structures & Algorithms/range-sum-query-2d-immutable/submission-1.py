class NumMatrix:
    # prefix sum 2d
    # prefix is 2d so each grid is sum of a rectangle ending at that position

    def __init__(self, matrix: List[List[int]]):
        # Time O(m*n)
        # Space O(m*n)
        row, col = len(matrix), len(matrix[0])
        # create a prefix 2d matrix with 0 padding
        self.prefix = [[0 for _ in range(col+1) ] for _ in range(row +1)]
        self.matrix = matrix
        for r in range(row):
            running_sum = 0
            for c in range(col):
                running_sum += self.matrix[r][c]
                above = self.prefix[r][c+1]
                self.prefix[r+1][c+1] = running_sum + above


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Time O(1)
        # Space O(1)
        # r1 = 0, col1 =0, r2 = 1, c2 =1 in the original index
        bottomRight = self.prefix[row2+1][col2+1]
        topRight = self.prefix[row1][col2+1]
        bottomLeft = self.prefix[row2+1][col1]
        topLeftCorner = self.prefix[row1][col1]

        return bottomRight - topRight - bottomLeft + topLeftCorner
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)