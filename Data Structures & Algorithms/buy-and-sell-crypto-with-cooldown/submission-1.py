class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # do we have a recursive solution for this?
        # profit(index, buy_price)
        # base case? index > len(prices), return 0
        # how to compute the profit?
        # how many decsions can we have? 
            # on a day if we did not buy previously, we can
                # buy the current day
                # skip the current day
            # on a day if we bought previously, we can
                # sell on the current day and get a profit
                # skip the current day
            # if we sell, we cannot buy the next day!
        
        # O(n^2) in time
        # O(n^2) in space
        memo = {}
        def profit(index, buy_price):
            if index >=len(prices):
                return 0
            if (index, buy_price) in memo:
                return memo[(index, buy_price)]
            # buy_price == -1
            # This means you currently do not hold any stock 
            # and are considering whether to buy or skip on the current day.
            if buy_price == -1: 
                # buy the current day
                buy = profit(index+1, prices[index])
                # skip the current day
                noBuy = profit(index+1, -1)
                maxProfit = max(buy, noBuy)
                memo[(index, buy_price)] = maxProfit
                return maxProfit
            
            # buy_price != -1
            # This means you currently hold a stock 
            # and are considering whether to sell or skip on the current day.
            if buy_price != -1: # indication we bought previously
                # sell on the current day and get a profit, we cannot buy the next day
                # If you sell on day i, you can't buy again on day i+1, we skip to i+2 day
                sellProfit = prices[index] - buy_price + profit(index+2, -1)
                # skip the current day
                noSellProfit = profit(index+1, buy_price)
                maxProfit = max(sellProfit, noSellProfit)
                memo[(index, buy_price)] = maxProfit
                return maxProfit
        ans = profit(0,-1)
        return ans