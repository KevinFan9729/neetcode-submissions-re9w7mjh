class Solution:
    def climbStairs(self, n: int) -> int:
        path_count = 0
        def climbStairs_count(step_sum: int):
            nonlocal path_count
            if step_sum == n:
                path_count += 1
                return # stop the function
            if step_sum < n:
                climbStairs_count(step_sum+1)
                climbStairs_count(step_sum+2)
            if step_sum > n:
                return 
        climbStairs_count(0)
        return path_count