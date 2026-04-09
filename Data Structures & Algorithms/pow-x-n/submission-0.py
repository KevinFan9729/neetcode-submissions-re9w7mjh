class Solution:
    def myPow(self, x: float, n: int) -> float:
        # pow (x,n) means the number x mutiply by itself
        # n times
        # why don't we just use a loop?
        # note if n is negative,
        # then x needs to become 1/x

        ans = 1
        if n < 0:
            x = 1/x
            n = abs(n)
        for _ in range(n):
            ans *= x
        return ans
        