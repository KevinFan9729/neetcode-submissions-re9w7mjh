class Solution:
    def integerBreak(self, n: int) -> int:
        # how to perform the "break" operation???
        # n = 4
        # 1+1+2 or 1+1+1+1
        # so say at every step we can break the int n from 1 to n-1 (cant be 0 to n as we will get 0 and k >=2)
        # we can define a function which return the max product given n
        # we have n unqiue state
        # for a state, we may compute using upto n step
        # Time O(n^2)
        # Space O(n)
        memo = {}
        def findMax(n):
            if n == 1:
                return 1
            if n in memo:
                return memo[n]
            maxProd = 1
            for j in range(1, n):
                # possible break
                # we can break further or use as it is (no more break)
                choice = j* max(findMax(n-j), n-j)
                maxProd = max(maxProd, choice)
            memo[n] = maxProd
            return maxProd

        res = findMax(n)
        return res