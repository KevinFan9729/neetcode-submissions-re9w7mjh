class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # A xor A = 0
        # 0 xor B = B
        # A xor B xor A = B
        # O(n) in time
        # O(1) in space
        ans = 0
        for i in range(len(nums)):
            ans ^= nums[i]
        
        for i in range(len(nums)+1):
            ans ^= i
        
        return ans