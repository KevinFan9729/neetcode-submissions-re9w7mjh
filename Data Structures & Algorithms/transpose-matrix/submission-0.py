class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # tanspose of say row * col matrix will have a shape of col*row
        # e.g 4*3 matrix will have a transpose of 3*4
        # Time O(m*n)
        # Space O(m*n) including output size
        row, col = len(matrix), len(matrix[0])
        # initialize col*row array 
        res  = [[0 for _ in range(row)] for _ in range(col)]
        for i in range(row):
            for j in range(col):
                res[j][i] = matrix[i][j]

        return res
