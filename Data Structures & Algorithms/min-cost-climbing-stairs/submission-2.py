class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        floor_num = len(cost)
        dp = [0] * (floor_num +1) # the extra represents overshot
        dp[floor_num-1] = cost[floor_num-1] # at exactly top, the top is always cost[len(cost)-1]
        for i in range(floor_num-1, 0, -1):
            dp[i-1] =  cost[i-1] + min(dp[i], dp[i+1])
        return min(dp[0],dp[1])