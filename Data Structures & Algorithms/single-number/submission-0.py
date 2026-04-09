class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        prev = 0
        for num in nums:
            prev = num ^ prev
        return prev