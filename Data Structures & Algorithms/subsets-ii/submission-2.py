class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        nums.sort() # group all duplicate together
        def dfs(i):
            if i >= len(nums): # run out of number
                res.append(curr.copy())
                return
            # include the current num
            curr.append(nums[i])
            dfs(i + 1)
            curr.pop()
            # excluding the current num
            while i + 1 < len(nums) and nums[i] ==nums[i+1]:
                i = i + 1 # exculde the duplicate num
            dfs(i + 1)
        
        dfs(0)
        return res
