class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            if n & 1: # 0000001 and n, this will give 1 if and only if n's 1's place is a 1
                count+=1
            n = n>>1 # right shift by 1
        return count
        