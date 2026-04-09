class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # two choices, include or not include the number in the result
        res = []
        subset = []
        def helper(i: int):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            #include nums[i]
            subset.append(nums[i])
            helper(i+1)
            subset.pop() # back track

            #not include nums[i]
            helper(i+1)

        helper(0)

        return res