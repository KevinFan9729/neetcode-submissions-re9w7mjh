class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # at each step we can either include the current
        # exclude the current
        # Time O(n * 2^n)
        # Space O(n)
        res = []
        curr = []
        def gen(i):
            if i >= len(nums):
                res.append(curr[:])
                return
            
            # include
            curr.append(nums[i])
            gen(i+1) # move on to the next 
            curr.pop()
            #exclude
            gen(i+1)
        
        gen(0)
        return res