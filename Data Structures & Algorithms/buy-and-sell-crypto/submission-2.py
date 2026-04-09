class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # find the lowest day to buy in
        L = 0
        profit = 0
        lowest = prices[0]
        for price in prices:
            if price< lowest:
                lowest = price
            profit = max (profit, price-lowest)
        return profit
