class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # oh we can only take from the front now
        # but we can take 1 <= X <= 2M stones
        # function defines maximum stones current player can get from piles[start:]
        # findMax(start, m)
        # [3,1,2,5,7]
        # [18, 15, 14, 12, 7]
        # suffix can let us quickly find remaining piles
        # Time O(n^2*m)
        # Space O(n*m)
        n = len(piles)
        suffix = [0] * n
        currSum = 0
        for i in range(n-1, -1, -1):
            currSum += piles[i]
            suffix[i] = currSum
        memo = {}
        def findMax(start, m):
            if start >= n:
                return 0
            if start == n - 2:
                # only two stones left
                # player can take the rest
                return suffix[start]
            if (start, m) in memo:
                return memo[(start, m)]
            maxVal = 0
            for x in range(1, 2*m+1):
                # x is number of piles 
                opponent = findMax(start + x, max(m, x))
                # suffix[start] is what is avaliable - opponent -> what we have
                current = suffix[start] - findMax(start + x, max(m, x))
                maxVal = max(maxVal, current)
            memo[(start, m)] = maxVal
            return maxVal
        
        res = findMax(0,1)
        return res
