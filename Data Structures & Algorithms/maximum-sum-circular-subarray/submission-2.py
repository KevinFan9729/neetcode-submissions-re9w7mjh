class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # this is like we can use the standard kadane for the middle ones
        # we can also track the min subarray sum (linear)
        # the cirlcuar sum can be sumTotal - min subarray sum (linear)
        # Time O(n)
        # Space O(1)
        totalSum = sum(nums)
        currSum = 0
        currSumMin = 0
        maxSum = nums[0]
        minSum = nums[0]
        for num in nums:
            currSum += num
            currSumMin += num
            maxSum = max(maxSum, currSum)
            minSum = min(minSum, currSumMin)
            currSum = max(currSum, 0)
            currSumMin = min(currSumMin, 0)
            
        if minSum == totalSum: # if this is true, it means the entire array is negative
            minSum = 0
        res = max(maxSum, totalSum - minSum)
        return res