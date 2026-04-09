class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # The problem states that the input array nums 
        # contains unique integers. Because every number 
        # is distinct, choosing a different combination of 
        # indices will always result in a different set of values.

        # we have two chocies at each step
        # include the num in the sub set
        # do not include the num in the subset
        # Time O(2^n)
        # Space O(n) # depth of the recursion tree, if output is not counted

        res = []
        def dfs(i, curr):
            nonlocal res
            if i >= len(nums):
                res.append(curr[:]) # get the shallow copy of the curr
                return
            # include:
            curr.append(nums[i])
            dfs(i+1, curr)
            curr.pop() # backtrack
            # not include
            dfs(i+1, curr)
        dfs(0,[])
        return res