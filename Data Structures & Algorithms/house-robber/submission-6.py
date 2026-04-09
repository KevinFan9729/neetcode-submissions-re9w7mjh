from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        dp[len(dp)-2] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            rob_profit = nums[i] + dp[i + 2] # dp[i+2] skip the profit of robbing adjacent house 
            skip_profit = dp[i + 1]
            dp[i] = max(rob_profit, skip_profit)
        return dp[0]