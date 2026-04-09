class Solution:
    def myPow(self, x: float, n: int) -> float:
        # divide and conquer
        # say we want to compute 2^10
        # 2^10 = 2^5 * 2^5
        # 2^5 = 2*2^2 * 2^2
        # 2^2 = 2*2

        # base case, 
            # when x == 0 , return 0 instantly
            # when n == 0, return 1, as anyNum^0 =1
        # recursive step
            # res = pow(x*x, n // 2)
        # O(log(n)) in time
        # O(log(n)) in space due to the call stack
        def dividePow(x,n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            res = dividePow(x*x, n//2)
            if n%2: # not divisible by 2
                return x*res # like 2^5 = 2*2^2 * 2^2
            else: # divisible by 2
                return res # like 2^10 = 2^5 * 2^5
        if n < 0:
            n = abs(n)
            x = 1/x
        ans = dividePow(x,n)
        return ans
