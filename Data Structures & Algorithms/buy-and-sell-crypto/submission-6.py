class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window?
        # we will have left and right pointers
        # left is buy pointer
        # right is sell pointer
        # if buy < sell:
        # good we can make a profit, compute the profit and expand the window
        # if buy >= sell:
        # not good, we cannot make a profit, needs a better buy date, we will shrink the window
        # keep buy at the lowest price so far
        # Time O(n)
        # Space O(1)
        buy_ptr = 0
        max_val = 0
        for sell_ptr in range(1, len(prices)):
            buy_price = prices[buy_ptr]
            sell_price = prices[sell_ptr]
            if buy_price < sell_price:
                profit = sell_price - buy_price
                max_val = max(max_val, profit)
                sell_ptr +=1
            else:# buy price is too high (buy price is larger or equal to sell price)
                buy_ptr = sell_ptr # set this sell price as the best buy price (as it is lower than the current buy)
                sell_ptr +=1 # shift the window
        return max_val