class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # stop when we are at len(curr) == len(nums)?
        # but how do we revert back?
        # Time O(n!)
        # Space O(n)
        res = []
        seen = set()
        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            for j in range(len(nums)):
                # we need a loop here as the start can be any number inside of the input list
                if nums[j] not in seen:
                    curr.append(nums[j])
                    seen.add(nums[j])
                    dfs(curr)
                    pop_val = curr.pop() # backtrack
                    seen.remove(pop_val)
        dfs([])
        return res