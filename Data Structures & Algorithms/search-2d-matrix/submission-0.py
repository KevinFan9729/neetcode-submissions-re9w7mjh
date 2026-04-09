class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row_index in range(len(matrix)):
            if matrix[row_index][-1] > target: #target may be contained in this row!
                row = matrix[row_index]
                left, right = 0, len(row)-1
                while left <= right:# binary search
                    mid = left + (right - left)//2
                    if target > row[mid]:
                        left = mid + 1
                    elif target < row[mid]:
                        right = mid - 1
                    else:
                        return True
            elif matrix[row_index][-1] == target:
                return True
            else:
                continue # proceed to the nex row
        return False # do not find the target, by default return false
