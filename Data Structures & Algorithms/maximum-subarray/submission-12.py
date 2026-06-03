class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # up to a sum
        # subarrays are contiguous
        # if my sum is negative, then sum up to this point has no use
        # if that is the case, we can get a new start 
        # Time O(n)
        # Space O(1)
        currSum = 0
        maxSum = nums[0] 
        for num in nums:
            currSum += num
            maxSum = max(maxSum, currSum)
            if currSum < 0:
                currSum = 0 # new start 
        return maxSum