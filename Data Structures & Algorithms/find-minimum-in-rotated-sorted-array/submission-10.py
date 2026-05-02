class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Time O(logn)
        # Space O(1)
        left, right = 0, len(nums)-1

        while left < right:
            mid = left + (right-left)//2
            if nums[mid] < nums[right]:
                # we are in a sorted portion
                # min is possible on the left
                # mid is also a possible candidate for min
                right = mid
            else:
                # min is in the right side
                left = mid+1
        
        return nums[left]