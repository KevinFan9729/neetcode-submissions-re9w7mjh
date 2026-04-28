class Solution:
    def getSum(self, a: int, b: int) -> int:
        # bit operations
        # Time O(1) at most 32 bit shifting
        # Space O(1)
        MASK = (1 << 32) - 1 # 11111111111111...
        sign = 1 << 31 # 100000000000...
        ans = 0
        while b !=0:
            # use xor to sum over all bits without carry
            # then later is this partial sum summing with carry
            partSum = (a ^ b) & MASK 
            # next carry
            carry = ((a & b) << 1) & MASK
            a = partSum
            b = carry
        ans = a
        return ans if (ans & sign) == 0 else -((~ans&MASK)+1)