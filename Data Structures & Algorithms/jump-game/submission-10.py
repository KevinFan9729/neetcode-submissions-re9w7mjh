class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # [1,2,3,0,1] -> greedily take the max step does not work
        # every step we have nums[i] steps
        # recurisve function reach(i) where i is equal to the index
        # Time O(n^2)
        # Space O(n)
        memo = {}
        sys.setrecursionlimit(2000)
        def reach(i):
            if i >= len(nums) - 1:
                return True
            if i < len(nums) - 1 and nums[i] == 0:
                # this path is invalid
                return False
            if i in memo:
                return memo[i]
            
            canReach = False

            for step in range(1, nums[i]+1):
                canReach = reach(i+step)
                if canReach:
                    return True
            memo[i] = canReach
            return canReach
        
        res = reach(0)
        return res