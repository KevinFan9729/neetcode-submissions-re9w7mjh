class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # use xor
        # a xor a = 0
        # 0 xor b = b
        # [0,2]
        # [0,1,2]
        # we can ue xor to 'cancel' out duplicate
        # Time O(n)
        # Space O(1)
        xorRes = 0
        for i in range(len(nums)+1):
            if i == len(nums):
                xorRes ^= i
                continue
            xorRes ^= i^nums[i]
        
        return xorRes
