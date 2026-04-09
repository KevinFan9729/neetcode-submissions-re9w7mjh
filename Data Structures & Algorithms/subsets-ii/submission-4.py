class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Sort so duplicates are adjacent.
        # This lets us detect repeated values easily.
        #
        # At each recursion level, only let the first copy of a value
        # open a branch.
        #
        # In other words:
        # don't let a duplicate value start another branch at the same level
        # if the previous identical value already started one.
        #
        # Time: O(n * 2^n)   (not just O(2^n), because copying subsets costs up to O(n))
        # Aux space: O(n)    (recursion stack / current path, excluding output)
        # Output space: O(n * 2^n)
        nums.sort()
        res = []
        def dfs(start, curr):
            res.append(curr[:])
            for j in range(start, len(nums)):
                if j > start and nums[j] == nums[j-1]:
                    continue 
                #“I am not the first option at this level, 
                # and I have the same value as the option right before me.”
                # So only the first occurrence gets to create a branch.
                curr.append(nums[j])
                dfs(j+1, curr)
                curr.pop()
        dfs(0, [])
        return res