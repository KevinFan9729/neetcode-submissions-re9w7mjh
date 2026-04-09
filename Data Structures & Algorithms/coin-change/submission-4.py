class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # recursive solution?
        # coinCount(index, currSum)
        # base case if index >= len(coins), not valid return inf
        # base case if currSum == amount, return 0 valid
         # base case if currSum > amount, not valid return inf
        # at each step we can
            # include the current coin
            # exclude the current coin
        # O(n*m) in time, each (index, currSum) state is computed only once
        # O(n*m) in space due to the hashmap

        memo = {}
        def coinCount(index, currSum):
            if index >= len(coins):
                return float('inf')
            if currSum == amount:
                return 0
            if currSum > amount:
                return float('inf')
            if (index, currSum) in memo:
                return memo[(index, currSum)]

            # include the current coin
            includeCount = coinCount(index, currSum= currSum+coins[index]) + 1

            # exclude the current coin
            excludeCount = coinCount(index+1, currSum)

            count = min(includeCount, excludeCount)
            memo[(index, currSum)] = count
            return count

        count = coinCount(0, 0)
        if count != float('inf'):
            return count
        else:
            return -1