class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # O(n*n!)
        res = []
        def dfs(pers):
            if len(pers) == len(nums):
                res.append(pers.copy())
                return 
            for num in nums:
                if num in pers: # exclude num that is already in pers
                    continue
                pers.append(num)
                dfs(pers)
                pers.pop() # backtrack
        dfs([]) 
        return res