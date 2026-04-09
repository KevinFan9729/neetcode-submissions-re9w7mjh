class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # a ^ (b ^ c) = (a ^ b) ^ c, and a ^ b = b ^ a. 
        # say we have [3,2,3]
        # prev = 0 initially
        # 0^3^2^3 = 0^3^3^2 = 0^0^2 = 0^2 = 2
        prev = 0
        for num in nums:
            prev = num ^ prev
        return prev