class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # the array is sorted
        # the result is a subarray as a result
        # sliding window
        # we can shrink the window until we have the subarray length equal to k
        # [4 2 1 2]
        # Time O(n)
        # Space O(1)
        left, right = 0, len(arr) - 1
        while left <= right and right-left+1 >k:
            leftDiff = abs(arr[left] - x)
            rightDiff = abs(arr[right] - x)
            if leftDiff < rightDiff:
                right-=1
            elif leftDiff > rightDiff:
                left+=1
            else: # prefer the smaller original number
                right -=1
        
        return arr[left: right+1]