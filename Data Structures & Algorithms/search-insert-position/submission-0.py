class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # binary search
        # the only modification is when we do not find the target
        # we do not return None
        # instead we return where it will be inserted
        # Time O(logn)
        # Space O(1)
        
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left+ (right-left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # possible in the right side
                left = mid+1
            else:
                # possible in the left side
                right = mid-1
        
        # when we are here
        # we know that we do not find the target inside of the target
        return left
        