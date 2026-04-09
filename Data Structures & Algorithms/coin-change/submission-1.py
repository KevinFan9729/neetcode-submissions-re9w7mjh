class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def findMincoinNum(curr_sum: int) -> int:
            # Base cases
            if curr_sum in memo:
                return memo[curr_sum]
            if curr_sum == amount:
                return 0
            if curr_sum > amount:
                return float('inf')

            # Try all coins and take the minimum
            min_coin_num = float('inf')
            for coin in coins:
                min_coin_num = min(min_coin_num, 1 + findMincoinNum(curr_sum + coin))

            memo[curr_sum] = min_coin_num
            return memo[curr_sum]
        ans = findMincoinNum(0)
        if type(ans) == float:
            return -1
        return ans
    