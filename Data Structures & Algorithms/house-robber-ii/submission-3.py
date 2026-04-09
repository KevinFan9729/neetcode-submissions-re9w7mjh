class Solution:
    def rob(self, nums: List[int]) -> int:
        # 2*O(n)
        # solving linear house robber twice
        # but we true dp in each calculation
        if len(nums) == 1:
            return nums[0]
        dp_no_first = [0] * len(nums)
        dp_no_last = [0] * len(nums)
        dp_no_first[-2] = nums[-1]
        dp_no_last[-2] = nums[-2]
        exclude_first = nums[1:]
        exclude_last = nums[:-1]
        for i in range(len(exclude_first)- 2, -1, -1):
            # exclude first house
            rob_profit = exclude_first[i] + dp_no_first[i+2]
            skip_profit = dp_no_first[i+1]
            dp_no_first[i] = max(rob_profit, skip_profit)

            # exclude the last house
            rob_profit = exclude_last[i] + dp_no_last[i+2]
            skip_profit = dp_no_last[i+1]
            dp_no_last[i] = max(rob_profit, skip_profit)

        return max(dp_no_first[0], dp_no_last[0])
