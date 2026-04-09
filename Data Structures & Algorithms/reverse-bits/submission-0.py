class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        # idea, move the rightmost bit of the original to the leftmost of the res
        for i in range(32):
            # Extract the rightmost bit of n
            bit = n & 1
            # Shift the bit to its new position in the reversed result
            result = (result << 1) | bit
            # Right shift n to process the next bit
            n >>= 1
        return result