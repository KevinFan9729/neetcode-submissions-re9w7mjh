class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # at each step we can decide we include this number into the subset or not
        # Time O(n * 2^n)
        # Space O(n)
        curr = []
        res = []

        def gen(i):
            if i >= len(nums):
                res.append(curr[:])
                return
            # include nums[i]
            curr.append(nums[i])
            gen(i+1)
            curr.pop() # undo

            # not include nums[i]
            gen(i+1)
        
        gen(0)
        return res