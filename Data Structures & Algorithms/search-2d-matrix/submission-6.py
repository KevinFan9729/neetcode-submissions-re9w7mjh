class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # the trick is do binary search twice,
        # binary search for to find which row to use,
        # then binary search within the row

        # to determine row
            # we needs to check if the value is within the row
            # here mid is corresponding to row number, and we fixed it at the end of the matrix (mid, col_num)
            # left =0 right = row_num
            # if it is then break, we found the row
            # if not
                # if target is larger than mid matrix[mid,col_num]
                    # left = mid+1
                # else 
                    # right = mid -1
        # after the row is determine, the rest is standard binary search

        # Time O(log(m*n))
        # Space O(1)
        if not matrix or not matrix[0]:
            return False
        row_num, col_num = len(matrix), len(matrix[0])

        left, right = 0, row_num - 1
        target_row_idx = -1
        while left <= right:
            mid = left + (right - left) // 2

            if matrix[mid][0]  <= target <= matrix[mid][col_num -1]:
                target_row_idx = mid
                break
            else:
                if target > matrix[mid][col_num -1]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        if target_row_idx == -1:
            # cannot find a row that conatins target
            return False
        
        left, right = 0, col_num - 1
        target_row = matrix[target_row_idx]

        while left <= right:
            mid = left + (right - left) // 2

            if target_row[mid] == target:
                return True
            elif target > target_row[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        return False


