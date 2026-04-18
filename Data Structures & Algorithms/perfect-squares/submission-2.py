class Solution:
    def numSquares(self, n: int) -> int:
        # we can compute candidates up to n
        # then we can have a recursive func return what is the minimum number of squares needed to make up the remaining amount?
        # once we have candaites
        # we can loop through the candidates and try to get pick perfect square to get remian to 0 
        # def pick(remain)
        # Time O(n)
        # Space O(n)
        import sys
        sys.setrecursionlimit(100000)
        candidates = [1]
        num = 1
        while candidates[-1] < n:
            num+=1
            candidates.append(num*num)
        memo = {}
        def pick(remain):
            if remain < 0:
                return float('inf')
            if remain == 0:
                return 0
            if remain in memo:
                return memo[remain]
            minLength = float('inf')
            for item in candidates:
                minLength = min(minLength, 1 + pick(remain - item))
            memo[remain] = minLength

            return minLength

        res = pick(n)
        return res
            
