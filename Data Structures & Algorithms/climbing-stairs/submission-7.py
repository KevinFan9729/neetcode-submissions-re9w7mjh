class Solution:
    def climbStairs(self, n: int) -> int:
        # can be solved with recursion plus memo
        # at each step we have 2 cases
            # take 1 step
            # take 2 steps
        # Time O(n)
        # Space O(n)
        memo = {}
        def climb(stair):
            nonlocal memo
            if stair == n:
                # we have found a path
                return 1
            if stair > n:
                # exceeding the target is not a valid path
                return 0
            if stair in memo:
                return memo[stair]
            climb_one = climb(stair+1)
            memo[stair+1] = climb_one
            climb_two = climb(stair+2)
            memo[stair+2] = climb_two

            return climb_one + climb_two

        ans = climb(0)

        return ans