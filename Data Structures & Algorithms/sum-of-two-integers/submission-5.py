class Solution:
    def getSum(self, a: int, b: int) -> int:
        # use xor
        # convert to binary
        # result range is [-2000, 2000]
        # 12-bit signed range is [-2048, 2047]
        # a ^ b gives the result of adding them ignoring carry
        # (a & b) << 1 gives the carry bits that still need to be added
        # ∼x=−x−1
        # ∼x=−(x+1)
        # ~(a ^ MASK) convert 2'complment to regular negative number
        # Time O(n)
        # Space O(1)

        MASK = 0b111111111111
        SIGN = 1 << 11            # sign bit for 12-bit signed int 100000000000

        # fix at 12 bits
        a &= MASK
        b &= MASK

        while b != 0:
            carry = ((a & b) << 1) & MASK # carray for the next bit
            a = (a ^ b) & MASK
            b = carry

        return a if a < SIGN else ~(a ^ MASK)