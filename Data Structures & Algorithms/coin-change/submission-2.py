class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # at the current sum, how many more coins do you need to reach the target
        memo = {}
        def findMincoinNum(coin_index, curr_sum):
            if curr_sum in memo:
                return memo[curr_sum]
            if coin_index >= len(coins):
                return float('inf')
            if curr_sum == amount:
                return 0 # (no more coins needed)
            if curr_sum > amount: # not a valid path
                return float('inf')
            
            # two decision,
            # include the current coin
            include = 1 + findMincoinNum(coin_index, curr_sum=curr_sum+coins[coin_index])
            # not include the current coin
            exclude = findMincoinNum(coin_index+1, curr_sum)

            min_coin_num = min(include, exclude)
            memo[curr_sum] = min_coin_num

            return min_coin_num
        ans = findMincoinNum(0, 0)
        print(memo)
        if type(ans) == float:
            return -1
        return ans
    