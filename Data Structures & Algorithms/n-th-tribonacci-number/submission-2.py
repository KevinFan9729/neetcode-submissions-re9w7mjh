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
        # Space O(1)
        # t0, t1, t2
        # we know up to t2
        a = 0
        b = 1
        c = 1
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        res = 0
        for i in range(n-2):
            res = a+b+c
            a,b,c = b,c,res # update the pointers by swapping; love python here!
        return res