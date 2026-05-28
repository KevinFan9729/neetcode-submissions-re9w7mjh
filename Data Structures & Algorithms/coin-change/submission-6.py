class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # unlimited number of each coin
        # we can keep reusing the same coin if needed
        # it is invalid say what we have > amount 
        # valid if what we have  == amount
        # At each setp, we can include or exclude a coin
        # the function return minimum additional coins needed
        # Time O(n^2)
        # Space O(n^2)
        memo = {}
        def find(i,curr):
            if i >=len(coins):
                return float('inf')
            if curr > amount:
                # invalid
                return float('inf')
            if curr == amount:
                # valid
                return 0
            if (i,curr) in memo:
                return memo[(i,curr)]
            
            # include
            # we do not incremnet i as we can include infinite number of the same coin
            include = 1 + find(i, curr+coins[i])
            # exclude
            exclude = find(i+1, curr)

            minCount = min(include, exclude)

            memo[(i,curr)] = minCount 
            return minCount

        res = find(0,0)
        return res if res != float('inf') else -1
