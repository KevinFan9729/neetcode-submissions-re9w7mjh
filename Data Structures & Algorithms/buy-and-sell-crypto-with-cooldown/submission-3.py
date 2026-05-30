class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # ok so if we sell, then we cannot buy on the next day
        # meaning if we sell, the next day we cannot do anything (skip)
        # define a function which return a max profit
        # if we bought before
        # then we can sell or skip
        # if we never bought anything before
        # we can buy or skip
        # Time O(n)
        # Space O(n)
        memo = {}
        def findMax(i, hold):
            if i >= len(prices):
                return 0
            if (i, hold) in memo:
                return memo[(i, hold)]
            
            maxVal = 0
            sell = 0
            buy = 0
            if hold:
                # we bought a stock before
                sell = prices[i] + findMax(i+2, False)# we have one day of cooldown
            else:
                # we dont hold a stock
                buy = findMax(i+1, True) - prices[i]
            
            skip = findMax(i+1, hold)
            maxVal = max(maxVal, buy, sell, skip)
            memo[(i,hold)] = maxVal
            return maxVal

        return findMax(0,False)