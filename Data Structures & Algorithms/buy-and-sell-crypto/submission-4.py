class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left is in the past, right is in the future 
        left, right = 0, 1
        maxValue = 0
        while left < right and right <len(prices):
            if prices[left] >= prices[right]:# will not make money or lose money
                left = right
            else:
                profit = prices[right] - prices[left]
                maxValue = max(profit, maxValue)
            right+=1
        return maxValue