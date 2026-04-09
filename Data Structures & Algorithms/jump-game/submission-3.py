class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        def jump(index):
            if index >= len(nums) -1: # reach the target!
                return True
            if nums[index] == 0: # cannot proceed
                return False
            if index in memo:
                return memo[index]
            max_jum = nums[index]
            for jump_len in range(max_jum, 0, -1):
                res = jump(index + jump_len)
                if res:
                    return True
            memo[index] = res
            return res
        return jump(0)