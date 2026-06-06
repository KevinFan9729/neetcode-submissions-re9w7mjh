class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if we want to find min in O(logn) time
        # this means we need to do it with binary search
        # but binary search only works on sorted data right?
        # we still have 2 parts of sorted array
        # if we compare mid with right
            # if mid > right
            # this means min can be in the right part of the array
            # else means that min can be mid itself or to the left
        # Time O(logn)
        # Space O(1)
        left, right = 0, len(nums) -1

        while left < right: # when left == right, we stop, as left will be pointing at mid
            mid = left + (right-left)//2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]