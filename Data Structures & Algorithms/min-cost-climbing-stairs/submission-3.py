class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # at each step, you can have 1 step or two steps
        def minCostClimb(curr_index):
            if curr_index > len(cost)-1: # no cost when we overshot
                return 0
            if curr_index in memo:
                return memo[curr_index]
            #choice 1 After paying the cost, you can step to (i + 1)th floor
            one_step_cost = cost[curr_index]+ minCostClimb(curr_index+1)
            #choice 2 After paying the cost, you can step to (i + 2)th floor
            two_step_cost = cost[curr_index]+ minCostClimb(curr_index+2)
            minCost = min(one_step_cost, two_step_cost)
            memo[curr_index] = minCost
            return minCost
        memo = {}
        startAt0 = minCostClimb(0)
        startAt1 = minCostClimb(1)
        ans = min(startAt0, startAt1)
        return ans