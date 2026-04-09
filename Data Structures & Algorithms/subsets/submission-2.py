from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

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
            dfs(i+1)
        dfs(0)
        return res
