class Solution:
    def climbStairs(self, n: int) -> int:
        # at n (the target) you have 0 way of reaching the target (you are already there! Skip this)
        # at n-1, you have 1 way of reaching the target
        # at n-2 you have you have 2 ways of reaching the target
        # at n-3 you have previous two steps of way of reaching the target
        if n == 1:
            return 1
        dp = [0]* n
        dp[-1] = 1 # at n-1 step
        dp[-2] = 2 # at n-2 step
        for i in range(n-3, -1, -1):
            dp[i] = dp[i+1]+dp[i+2]
        return dp[0]