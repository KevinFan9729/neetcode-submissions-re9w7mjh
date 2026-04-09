class Solution:
    def rob(self, nums: List[int]) -> int:
        # 2*O(n)
        # solving linear house robber twice
        # but we have memoization here
        if len(nums) == 1:
            return nums[0]
        def getMaxProfit(curr_index: int, house_val: List[int]) -> int:
            if curr_index >= len(house_val):
                return 0
            if curr_index in memo:
                return memo[curr_index]
            rob_profit = house_val[curr_index] + getMaxProfit(curr_index + 2, house_val)
            skip_profit =  getMaxProfit(curr_index + 1, house_val)
            profit = max(rob_profit, skip_profit)
            memo[curr_index] = profit
            return profit
        exclude_first = nums[1:]
        exclude_last = nums[:-1]
        memo = {}
        max_profit_exclude_first = getMaxProfit(0, exclude_first)
        memo = {}
        max_profit_exclude_last = getMaxProfit(0, exclude_last)
        ans = max(max_profit_exclude_first, max_profit_exclude_last)
        return ans
