class Solution:
    def countBits(self, n: int) -> List[int]:
        # O(n) in time
        # O(n) in space
        dp = [0] * (n+1)
        offset = 1
        # offsets are most signicant bit: 1, 2, 4, 8, 16 ...

        for i in range(1, n+1):
            if offset*2 == i:
                offset = i
            dp[i] = 1 +dp[i-offset]
        return dp