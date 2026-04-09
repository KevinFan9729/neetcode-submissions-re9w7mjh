class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # O(n^2) in time
        # O(1) in space

        left, right = 0, len(matrix) -1

        while left < right:
            for i in range(right-left):
                top, bottom = left, right


                # save top right
                topRight = matrix[top+i][right]
                # move topleft to top right
                matrix[top+i][right] = matrix[top][left+i]

                # save bottom right
                bottomRight = matrix[bottom][right-i]
                # move topRight to bottom right
                matrix[bottom][right-i] = topRight


                # save bottom left
                bottomLeft = matrix[bottom-i][left]
                # move bottomRight to bottom left
                matrix[bottom-i][left] = bottomRight

                # move bottomLeft to top left
                matrix[top][left+i] = bottomLeft

            left+=1
            right-=1
        