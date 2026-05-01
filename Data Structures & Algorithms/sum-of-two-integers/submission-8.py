class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Time O(1)
        # Space O(1)
        MASK = (1 << 32) - 1  #11111111....11111
        SIGN = 1 << 31

        while b != 0:
            carry = ((a & b) << 1 ) & MASK
            a = (a ^ b) & MASK
            b = carry

        return a if (a & SIGN) == 0 else -(((~a)&MASK) +1)