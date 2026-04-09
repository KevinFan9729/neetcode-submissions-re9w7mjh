class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # slding window variable length
        L = 0
        profit = 0
        for R in range(len(prices)):
            while prices[R] < prices[L] and L < R: # not making a profit
                L += 1 # choose another day to buy
            profit = max(profit, prices[R]-prices[L])
        return profit
