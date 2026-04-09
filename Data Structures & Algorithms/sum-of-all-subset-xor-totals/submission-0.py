class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # at each step
        # we have two choices
            # 1.include the number into the subset
            # 2.exclude the number into the subset
        # Time O(2^n)
        # Space O(n)
        if len(nums) == 0:
            return 0
        # return the sum of xor
        def dfs(i, currXor):
            if i >= len(nums): # done forming a subset
                return currXor
            include = dfs(i+1, nums[i]^currXor)
            exclude = dfs(i+1, currXor)
            return include + exclude

        return dfs(0,0)