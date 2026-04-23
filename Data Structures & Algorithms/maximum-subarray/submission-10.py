class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane 
        # discard neg sum as they will not contribute

        currSum = 0
        maxSum = nums[0]

        for num in nums:
            currSum += num
            maxSum = max(maxSum, currSum)
            currSum = max(currSum, 0)
        return maxSum