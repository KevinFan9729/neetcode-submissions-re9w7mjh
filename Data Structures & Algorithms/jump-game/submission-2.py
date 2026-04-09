class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def jump(index):
            if index >= len(nums) -1: # reach the target!
                return True
            if nums[index] == 0: # cannot proceed
                return False
            max_jum = nums[index]
            for jump_len in range(max_jum, 0, -1):
                res = jump(index + jump_len)
                if res: # early stop
                    return True
            return res
        return jump(0)