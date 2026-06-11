class Solution:
    def integerBreak(self, n: int) -> int:
        # how do I brek the integer?
        # so the breaking is kinda of like wea have choices?
        # 1,2,3 n-1 -> all the number we can pick to break into
        # I need to know at each step, what is the number we are mutiplying (breaking into)
        # we can define a function where say we return the maxproduct starting at breaking num
        # Time O(n^2)
        # Space O(n)

        memo = {}
        def maxProduct(num):
            if num == 1:
                return 1
            # if num < 1:
            #     # invalid
            #     return 0
            if num in memo:
                return memo[num]
            
            maxProd = 1
            for i in range(1,n):
                # if we break i out of num
                # num must subtract that i
                # we can continue to break or we can just stop breaking
                if num > i:
                    continueBreak = i * maxProduct(num-i)
                    stopBreaking = i* (num-i)
                    maxProd = max(maxProd, continueBreak, stopBreaking)
            memo[num] = maxProd
            return maxProd

        res = maxProduct(n)
        return res