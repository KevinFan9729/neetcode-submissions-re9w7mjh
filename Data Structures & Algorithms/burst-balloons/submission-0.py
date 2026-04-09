class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Add 1 at both ends to simplify the boundary conditions
        nums = [1] + nums + [1]
        n = len(nums)
        
        # Memoization table, where dp[left][right] is the max coins we can collect
        # from bursting all balloons between indices left and right (exclusive).
        memo = {}
        
        def burst(left, right):
            maxVal = 0
            # Base case: no balloons to burst between left and right
            if left + 1 == right:
                return 0
            # If already computed, return the memoized result
            if (left, right) in memo:
                return memo[(left, right)]
            
            # Try bursting each balloon between left and right as the last one
            for i in range(left + 1, right):
                coins = nums[left] * nums[i] * nums[right]  # Coins from bursting the i-th balloon
                coins += burst(left, i)  # Coins from the left side
                coins += burst(i, right)  # Coins from the right side
                maxVal = max(maxVal, coins)
                memo[(left, right)] = maxVal
            
            return maxVal
        
        # Burst all balloons between 0 and n-1
        return burst(0, n - 1)
