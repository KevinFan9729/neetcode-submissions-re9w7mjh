class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        nums.sort() # sort to group all duplicates together

        def dfs(i: int):
            # base case
            if i >= len(nums):
                res.append(curr.copy())
                return
            # two choices
            # choice 1: add a number into the list
            curr.append(nums[i])
            dfs(i+1)
            curr.pop() #backtrack
            # choice 2: do not add a number into the list
            while i < len(nums) -1:
                if nums[i] == nums[i+1]: # duplicate found 
                    i = i+1 # skip the duplicate
                else:
                    break
            dfs(i+1)
        dfs(0)
        return res