class Solution:
    def climbStairs(self, n: int) -> int:
        # O(n)
        memo = defaultdict(int)
        def climbStairs_count(step_sum: int):
            if step_sum in memo:
                return memo[step_sum]
            if step_sum == n:
                return 1
            if step_sum > n:
                return 0
            if step_sum < n:
                memo[step_sum] += climbStairs_count(step_sum+1)
                memo[step_sum] += climbStairs_count(step_sum+2)
            return memo[step_sum]
        ans = climbStairs_count(0)
        return ans