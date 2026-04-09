class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # can we solve this recursively
        # jump(index)
        # base case
            # if index == len(nums)-1, good we reach the target, return True
            # if nums[index] == 0 and index != len(nums)-1, cannot reach the last index, return False
        # at each index we can jump (1-maxJump) length
        # O(maxJump^n) in time as we can jump (1-maxJump) steps so
        # O(n) in space as this is the size of the call stack

        def jump(index):
            if index == len(nums) -1:
                return True
            if nums[index] == 0 and index != len(nums)-1:
                return False
            
            maxJump = nums[index]
            for length in range(1, maxJump+1):
                if jump(index + length):
                    return True
            return False
        ans = jump(0)
        return ans