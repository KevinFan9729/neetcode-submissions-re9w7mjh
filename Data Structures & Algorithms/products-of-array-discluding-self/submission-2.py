import copy
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # compute the prefix product list
        # compute the sufix product list
        # compute the result at left of prefix i index * right of suffix i index
        prefix = copy.copy(nums)
        suffix = copy.copy(nums)
        
        for i in range(1, len(nums)):
            prefix[i] = prefix[i]* prefix[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i]* suffix[i+1]

        res = [0] * len(nums)
        for i in range(len(nums)):
            left_indx = i - 1
            right_indx = i + 1
            if left_indx < 0:
                left_val = 1
            else:
                left_val = prefix[left_indx]
            if right_indx > len(nums) - 1:
                right_val = 1
            else:
                right_val = suffix[right_indx]
            
            res[i] = left_val * right_val

        return res