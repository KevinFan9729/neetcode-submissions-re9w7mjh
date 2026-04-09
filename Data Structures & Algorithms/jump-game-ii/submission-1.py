class Solution:
    def jump(self, nums: List[int]) -> int:
        # recursive function to reach to the target
        # take the curr index
        # let's frist tink about how to determine if you can reach the target
        # you reach the target when index >= len(nums) - 1
        # you cannot reach the target when you end up a position where nums[index] == 0 and index < len(nums) - 1
        # O(k^n), where k is the maximum jump length allowed. n is the size of array
        # O(n) space, callstack
        min_count = float("inf")
        jump_count = 0
        def JumpCount(index):
            nonlocal jump_count, min_count
            if index >= len(nums) -1:
                min_count = min(min_count, jump_count)
                return
            max_jump_len = nums[index]
            if max_jump_len == 0 and index < len(nums) -1:
                return
            for possible_jump_len in range(max_jump_len, 0, -1):
                jump_count += 1
                JumpCount(index+possible_jump_len)
                jump_count -= 1
            return
        JumpCount(0)
        return min_count
