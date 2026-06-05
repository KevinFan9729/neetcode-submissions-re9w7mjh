class Solution:
    def numSquares(self, n: int) -> int:
        # given n, we can start from 1 end at rounup(n**0.5) to create possible perfect squares
        # we can then define a function which return minimum number of perfect squares needed to reach n from currSum
        # we can includ ethe same perfect square repeatively
        # currSum is bounded by the 0...n
        # to compute each currSum we need 1 to sqrt(n) steps
        # Time O(n*sqrt(n))
        # Space O(m)
        sys.setrecursionlimit(100000)
        memo = {}
        def findMin(currSum):
            if currSum > n:
                return float('inf')
            
            if currSum == n:
                return 0

            if currSum in memo:
                return memo[currSum]

            minVal = float('inf')

            for i in range(1, int(math.ceil(n**0.5))+1):
                perfectSquare = i*i
                check = 1+ findMin(currSum + perfectSquare)
                minVal = min(minVal, check)
            memo[currSum] = minVal
            return minVal
        
        res = findMin(0)
        return res