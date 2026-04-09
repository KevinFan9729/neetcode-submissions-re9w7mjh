class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # two decisions at each index i
         # include num[i] in the solution
         # not include num[i] in the solution 
        res, curr = [], []
        def helper(i, nums, res, curr):
            if i >= len(nums): #out of bound
                res.append(curr.copy())
                return # get out of the function

            # decision 1
            # include nums[i]
            curr.append(nums[i])
            helper(i+1, nums, res, curr)
            curr.pop() # back track

            # decision 2
            # not to include nums[i]
            helper(i+1, nums, res, curr)
        helper(0, nums, res, curr)
        return res