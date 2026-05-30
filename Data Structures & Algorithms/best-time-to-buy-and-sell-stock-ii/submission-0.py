class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # you can but and tehn immediately sell it on the same day???
        # buying and then immediately selling on the same day gives profit 0, because there is only one price for that day
        # this means there is no cooldown
        # effecitively at each step we can either buy or sell
        # but if you dont have anything you cannot sell
        # if you bought something, you canot buy anymore you must sell

        # on a day we can also skip (hold), this means we dont buy nor sell
        # we want max profit
        # The maximum additional profit we can make from day i to the end,
        # given our current state:
        # - holding = True: we currently own 1 stock
        # - holding = False: we currently own 0 stock
        # Time O(n) i can be n, and say holding is binary
        # Space O(n)
        memo = {}
        def findMax(i, holding):
            if i >= len(prices):
                return 0

            if (i,holding) in memo:
                return memo[(i,holding)]
            
            sell = 0
            buy = 0
            maxP = 0
            # chocies:
            # if we have holding, we can either sell or keep holding on the day
            if holding:
                sell = prices[i] + findMax(i+1, holding = False)

            # if we dont have any holding, we can skip or buy something
            else:
                buy = findMax(i+1, holding = True) - prices[i]
            
            skip = findMax(i+1, holding)

            maxP = max(maxP, buy, sell, skip)
            memo[(i,holding)] = maxP
            return maxP

        res = findMax(0,0)
        return res
