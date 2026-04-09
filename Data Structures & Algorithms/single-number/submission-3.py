class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # use bitwise xor
        # num1^num1 = 0
        # and 0^num2 = num2
        # Time O(n)
        # Space O(1)
        res = 0
        for num in nums:
            res^=num
        return res