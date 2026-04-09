class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # two choices at each step
            # take 1 step
            # take 2 steps
        # can be solved with recursion
        # use dfs(curr) or dfs(curr, price)?
        # What is the function returning? 
            #  1 the func should return min price,
        # Does the future answer change if I change this variable? 
            # 2 no min price is min price at any step 
        # Is this variable a constraint or just a history/accumulator?" 
            # 3 if we add price to the recursion argument, it will be a accumulator. 
        # verdict, do not take price as a function argument just use dfs(curr)
        # Time O(n)
        # Space O(n)
        memo = {}
        def dfs(curr):
            if curr >= len(cost):
                return 0
            if curr in memo:
                return memo[curr]
            
            # pay the current price
            price = cost[curr]+min(dfs(curr+1), dfs(curr+2))

            # record the current min
            memo[curr] = price

            return price
        start_0 = dfs(0)
        start_1 = dfs(1)

        ans = min(start_0,start_1)
        return ans