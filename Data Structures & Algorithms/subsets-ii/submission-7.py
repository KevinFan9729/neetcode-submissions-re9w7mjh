class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # exclude now needs special care
        # nums = [1, 2, 2]
        # Without special handling, you could generate [1, 2] in two different ways:

        # include the first 2, exclude the second 2
        # exclude the first 2, include the second 2
        nums.sort()
        curr = []
        res = []
        def gen(i):
            if i >= len(nums):
                res.append(curr[:])
                return
            
            # include current i
            curr.append(nums[i])
            gen(i+1)
            curr.pop()

            # exclude
            while i+1 <= len(nums) - 1 and nums[i+1] == nums[i]:
                # skip duplicate
                i+=1
            gen(i+1)
        gen(0)
        return res