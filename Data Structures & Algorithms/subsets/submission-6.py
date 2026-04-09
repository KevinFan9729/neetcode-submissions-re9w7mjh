class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # input is unique
        # at every step make a decsion 
            # include the current num into the subset
            # exclude the current num
        # Time O(2^n)
        # Space O(n)
        res = []
        def subsetGen(i, sub):
            if i >= len(nums):
                res.append(sub[:])
                return
            # include
            sub.append(nums[i])
            subsetGen(i+1, sub)
            sub.pop() # backtrack
            # exclude
            subsetGen(i+1, sub)
            
        
        subsetGen(0,[])
        return res
