class Solution:
    def climbStairs(self, n: int) -> int:
        # O(2^n)
        def climbStairs_count(step_sum: int):
            if step_sum == n:
                return 1
            if step_sum > n:
                return 0
            path_count = 0
            if step_sum < n:
                path_count += climbStairs_count(step_sum+1)
                path_count += climbStairs_count(step_sum+2)
            return path_count
        ans = climbStairs_count(0)
        return ans