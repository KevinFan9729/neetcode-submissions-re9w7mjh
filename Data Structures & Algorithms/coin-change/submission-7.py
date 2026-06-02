class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # for each step. we can try any of the coin denominations
        # define a recursive function, findMin(currSum) and this 
        # function return the min number of coins needed to reach
        # the target amount
        # Time: O(amount * len(coins))
        # Space: O(amount)
        memo = {}
        def findMin(currSum):
            if currSum == amount:
                # this is a valid path
                return 0
            if currSum > amount:
                # invalid
                return float('inf')
            if currSum in memo:
                return memo[currSum]
            minVal = float('inf')
            for coin in coins:
                minCoin = 1 + findMin(currSum + coin)
                minVal = min(minVal, minCoin)
            memo[currSum] = minVal
            return minVal
            
        res = findMin(0)
        return res if res != float('inf') else -1