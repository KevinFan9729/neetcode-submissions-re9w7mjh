class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # we can do a binary search
        # each row is sorted in acending order
        # we can see which row can the target be 
        rows, cols = len(matrix), len(matrix[0])

        if target > matrix[rows-1][cols-1]:
            return False

        for r in range(rows):
            if target <= matrix[r][cols-1]:
                if target == matrix[r][cols-1]:
                    return True
                break
        target_row = matrix[r]
        left, right= 0, len(target_row)-1
        while left <= right:
            mid = left + (right -left) //2
            if target_row[mid]> target:# search the left subarray
                right = mid - 1
            elif target_row[mid]< target:
                left = mid + 1
            else:
                return True
        return False

