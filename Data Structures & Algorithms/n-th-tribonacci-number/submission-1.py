class Solution:
    def tribonacci(self, n: int) -> int:
        # n = 3
        # t_6 = t_3 + t_4+ t_5
        # t_5 = t_2+ t_3+ t_4
        # t_4 = t_1 + t_2 + t_3
        # t_3 = t_0 + t_1 + t_2
        # feel like it is recursive???
        # lots of repeated work
        # use memo
        # Time O(n)
        # Space O(n)
        memo = {}
        def gen(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 1
            if n in memo:
                return memo[n]
            res = gen(n-3)+gen(n-2)+gen(n-1)
            memo[n] = res
            return res
        
        res = gen(n)
        return res