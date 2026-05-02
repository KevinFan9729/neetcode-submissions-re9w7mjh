class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # nums[i] is the MAX jump length at that pos,
        # so you can 1 to nums[i]
        # recursion
        # jump(i)
        # at i we have num[i] choices
        # time complexity is number of states × work per state
        # Time O(n^2)
        # Space O(n)
        sys.setrecursionlimit(2000)
        if nums[0] == 0 and len(nums)>1:
            return False
        memo = {}
        def jump(i):
            if i >= len(nums) -1:
                return True
            if nums[i] == 0:
                return False
            if i in memo:
                return memo[i]
            
            for j in range(1, nums[i]+1):
                nextJump = jump(i+j)
                if nextJump:
                    return True
            # only mark memo[i] = False after all jumps from i fail
            memo[i] = False
            return False

        res = jump(0)
        return res