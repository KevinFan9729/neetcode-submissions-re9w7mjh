class Solution:
    def rob(self, nums: List[int]) -> int:
        # two choices at each step, rob or not rob
        # top down dp
        # With memoization, each index is processed only once. The memo dictionary stores the result for each index
        # O(n)
        memo = {}
        def maxRobProfit(curr_index):
            if curr_index >= len(nums): # run out of houses to rob
                return 0 
            if curr_index in memo:
                return memo[curr_index]
            # choice 1, rob the current house, skip the adjacent house
            rob_profit = nums[curr_index] + maxRobProfit(curr_index+2)
            # choice 2, not to rob the current house
            no_rob_profit = maxRobProfit(curr_index+1)

            max_profit = max(rob_profit, no_rob_profit)
            memo[curr_index] = max_profit
            return max_profit
        ans = maxRobProfit(0)
        return ans
        