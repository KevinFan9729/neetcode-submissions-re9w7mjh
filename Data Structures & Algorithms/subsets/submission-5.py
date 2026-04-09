class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # at each step include or exclude the number
        # Time O(2^n)
        # Space O(n)
        res = []
        def dfs(i, curr):
            if i >=len(nums):
                res.append(curr[:])
                return
            # include
            curr.append(nums[i])
            dfs(i+1, curr)
            curr.pop()
            dfs(i+1, curr)
        dfs(0, [])
        return res