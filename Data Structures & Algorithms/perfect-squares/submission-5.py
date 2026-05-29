class Solution:
    def numSquares(self, n: int) -> int:
        # perfect squares are numbers where num**0.5 is an int
        # or when we have a normal number i
        # i*i is a perfect square
        # we want to add to n
        # so our search range is 1 to int(math.floor(sqrt(n)))
        # can we just try recursively all perfect square?
        # def find(currSum) # this function return min number of perfect square that reach n
        # Time O(n*sqrt(n)) ok, we have n unique state, to compute each state, we may run sqrt(n) times (inner loop)
        # Space O(n)
        sys.setrecursionlimit(100000)
        memo = {}
        def find(currSum):
            if currSum > n:
                # invalid!
                return float('inf')
            if currSum == n:
                # valid path
                return 0
            if currSum in memo:
                return memo[currSum]
            minCount = float('inf')
            # a perfect square can be used repeatively
            for i in range(1, int(math.floor(n**0.5)+1)):
                perfect = i*i
                res = 1 + find(perfect + currSum)
                minCount = min(minCount, res)
            memo[currSum] = minCount
            return minCount
        ans = find(0)
        return ans