class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        floor_num = len(cost)
        # memoization solution
        # O(n)
        memo = {}
        def minCostStairs(curr):
            if curr >= floor_num:
                return 0
            if curr in memo:
                return memo[curr]
            cost_one_step = minCostStairs(curr+1)
            cost_two_steps = minCostStairs(curr+2)
            curr_cost = cost[curr] + min(cost_one_step, cost_two_steps)
            memo[curr] = curr_cost
            return curr_cost
        
        start_at_0 = minCostStairs(0)
        start_at_1 = minCostStairs(1)
        ans = min(start_at_0, start_at_1)
        return ans