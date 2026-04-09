class Solution:
    def jump(self, nums: List[int]) -> int:
        # time O(k*n) k is the maximum jump length
        # space O(n) the recursion could theoretically go as deep as the length of the array.
        memo = {}
        def JumpCount(index):
            # Base case: when we've reached or passed the last index
            if index >= len(nums) - 1:
                return 0
            max_jump_len = nums[index]
            if max_jump_len == 0 and index < len(nums) -1:
                return float("inf") # path is invalid, cannot move forward
            if index in memo:
                return memo[index]
            min_jumps = float("inf")
            for possible_jump_len in range(max_jump_len, 0, -1):
                jump_result = JumpCount(index + possible_jump_len)
                if jump_result != float("inf"):
                    min_jumps = min(min_jumps, 1 + jump_result)
            memo[index] = min_jumps
            return min_jumps
        res = JumpCount(0)
        return res
