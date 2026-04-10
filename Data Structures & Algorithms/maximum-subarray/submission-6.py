class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Time O(n)
        # Space O(n)
        
        memo = {}
        def bestSumI(i):
            if i == 0:
                return nums[i]
            if i in memo:
                return memo[i]
            
            expand = nums[i] + bestSumI(i-1)
            newStart = nums[i]
            maxSum = max(expand, newStart)
            memo[i] = maxSum
            return maxSum

        maxSum = nums[0]
        for i in range(len(nums)):
            maxSum = max(maxSum, bestSumI(i))
        return maxSum