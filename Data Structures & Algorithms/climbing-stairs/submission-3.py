class Solution:
    def climbStairs(self, n: int) -> int:
        # at each index, you can climb 1 or 2 steps
        memo = {}
        def climb(curr_pos):
            if curr_pos == n:
                return 1 # valid path
            if curr_pos > n:
                return 0 # not a valid path
            if curr_pos in memo:
                return memo[curr_pos]
            one_step_choice = climb(curr_pos + 1)
            two_step_choice = climb(curr_pos + 2)
            path_count = one_step_choice + two_step_choice
            memo[curr_pos] = path_count
            return path_count
        ans = climb(0)
        return ans