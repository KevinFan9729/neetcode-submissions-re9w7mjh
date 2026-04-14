class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # sliding window does not work here 
        # as we have negative values so it is not clear how to increase/decrease bounds
        # every step we can grow the subarray
        # or have a new start
        # Time O(n)
        # space O(n)
        memo = {}
        def bestSumAtI(i):
            if i == 0:
                return nums[0]
            if i in memo:
                return memo[i]
            # extend 
            extend = bestSumAtI(i-1) + nums[i]

            # new start
            newStart = nums[i]

            bestAtI = max(extend, newStart)
            memo[i] = bestAtI
            return bestAtI
        maxSum = nums[0]
        for i in range(len(nums)):
            maxSum = max(maxSum, bestSumAtI(i))
        return maxSum