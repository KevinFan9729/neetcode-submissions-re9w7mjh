class Solution:
    def numSquares(self, n: int) -> int:
        # we can compute candidates up to n
        # then we can have a recursive func return what is the minimum number of squares needed to make up the remaining amount?
        # once we have candaites
        # we can loop through the candidates and try to get pick perfect square to get remian to 0 
        # def pick(remain)
        # Time O(n * sqrt(n))
        # Space O(n)

        # let dp[x] mean the minimum number of perfect squares that sum to x
        # base case: dp[0] = 0
        # for each amount from 1 to n, try all square numbers <= amount
        # transition should mirror your recursive relation

        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                curr_s = j * j
                dp[i] = min(dp[i], 1 + dp[i - curr_s])
                j += 1

        return dp[n]
            
