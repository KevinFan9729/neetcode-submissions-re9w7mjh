class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # [1,1] not valid, no peak
        # I dont need to find the absolute peak
        # this means local peak is fine (just fine ONE peak)
        # log(n) means we need binary search
        # we can compute uphill
        # if say nums[mid] > nums[mid+1] this means left side is uphill
        # peak may be in the left
        # if say nums[mid] < nums[mid+1] then right side is uphill
        # peak may be in the right
        # assume we must have one peak in the array
        # Time O(logn)
        # Space O(1)
        n = len(nums)
        left, right = 0, n - 1

        while left <= right:
            mid = left + (right-left) // 2
            leftH = nums[mid-1] if mid-1 >= 0  else float('-inf')
            rightH = nums[mid+1] if mid+1 <= n-1  else float('-inf')
            if leftH < nums[mid] > rightH:
                return mid

            if  nums[mid] > nums[mid+1]:
                # leftward uphill
                right = mid - 1
            else:
                left = mid + 1