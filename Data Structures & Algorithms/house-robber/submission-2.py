from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def getMaxProfit(curr_index):
            if curr_index >= len(nums):
                return 0
            if curr_index in memo:
                return memo[curr_index]
            # to rob or not to rob
            # rob the current house
            rob_profit = nums[curr_index] +getMaxProfit(curr_index+2)
            # not to rob the current house
            skip_profit = 0 +getMaxProfit(curr_index+1)
            profit = max(rob_profit, skip_profit)
            memo[curr_index] = profit
            return profit
        ans = getMaxProfit(0)
        return ans