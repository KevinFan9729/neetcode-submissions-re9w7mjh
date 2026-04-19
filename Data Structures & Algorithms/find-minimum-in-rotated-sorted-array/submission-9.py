class Solution:
    def findMin(self, nums: List[int]) -> int:
        # needs to use binary search for O(logn)
        # we may have two sorted portion (or just one)
        # if mid val > right val
            # min is on the right sorted portion
        # if mid val < right val
            # we are in a sorted portion,
            # min can be mid Or further to the left
        # Time O(logn)
        # Space O(1)
        left, right = 0, len(nums)-1

        while left < right:
            mid = left + (right-left)//2
            print(left, right, mid)
            if nums[mid] > nums[right]:
                left = mid +1
            else:
                right = mid
        
        return nums[left]