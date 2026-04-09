class Solution:
    def climbStairs(self, n: int) -> int:
        # when you are at stair n, you get get there in 0 way (alreay there)
        # when you are at n-1, you can get there in 1 way (1 step)
        # when you are at n-2, you can get there in 2 ways (1+1 or 2 steps)
        memo = {}
        def climb(curr):
            if curr == n: # reach the target
                return 1 # one valid path to reach the top
            if curr >n:
                return 0
            if curr in memo:
                return memo[curr]
            count = climb(curr+1)+climb(curr+2)
            memo[curr] = count
            return count

        path_count = climb(0)
        return path_count
        