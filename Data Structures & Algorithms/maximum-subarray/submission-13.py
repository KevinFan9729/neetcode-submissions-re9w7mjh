class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # we can think of this recursively
        # at each step we can add the current number to the subarray sum
        # or have a new start
        # bestAtI maximum subarray sum ending exactly at index i
        # Time O(n)
        # Space O(n)
        memo = {}
        def bestATi(i):
            if i == 0:
                return nums[0]
            if i in memo:
                return memo[i]
            # extend
            extend = nums[i] + bestATi(i-1)
            # new start
            newStart = nums[i]
            maxSum = max(extend, newStart)
            memo[i] = maxSum
            return maxSum

        res = nums[0]
        for i in range(len(nums)):
            res = max(res, bestATi(i))
        return res