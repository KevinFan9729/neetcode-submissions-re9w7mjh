class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # unlimited number of each coin
        # we can keep reusing the same coin if needed
        # it is invalid say what we have > amount 
        # valid if what we have  == amount
        # At each current total, try every possible coin and take the minimum valid result.
        # the function return at the curr total, minimum additional coins needed
        # Time O(n)
        # Space O(n)
        memo = {}
        def find(curr):
            if curr > amount:
                # invalid
                return float('inf')
            if curr == amount:
                # valid
                return 0
            if curr in memo:
                return memo[curr]
            
            count = float('inf')
            for coin in coins:
                count = min(count, 1 + find(curr+coin))
            memo[curr] = count 
            return count

        res = find(0)
        return res if res != float('inf') else -1
