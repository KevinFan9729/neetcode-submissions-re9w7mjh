class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #[1 1 2] 
        # we will produce 1 2 and 1 2 (duplicate sets)
        # include first 1, and 2
        # include second 1 and 2
        # so when we decide to exlcude 1, we must exlcude all ones as those ones starting to include other numbers will casue duplicates
        # this is include the next valid number apporch instead of the include vs exlcude logic
        # At the same recursion level, skip duplicate values
        # so identical numbers do not start duplicate branches
        # Time O(n * 2^n)
        # Space O(n)
        nums.sort()
        curr = []
        res = []
        def gen(i):
            res.append(curr[:])
            for j in range(i, len(nums)):
                if j > i and nums[j-1] == nums[j]:
                    continue
                curr.append(nums[j])
                gen(j+1)
                curr.pop()
        gen(0)
        return res