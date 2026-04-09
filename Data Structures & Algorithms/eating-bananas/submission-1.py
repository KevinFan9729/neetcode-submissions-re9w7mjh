import math
class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        left = 1
        right = max(piles)
        res = float('inf')
        #O(nlogn)
        while left <= right:
            k = left + (right - left)//2
            tmp_hour = 0
            for i in piles:
                tmp_hour+= math.ceil(float(i)/k)
            if tmp_hour > h: # rate is too slow, must increase k
                left = k + 1
            else: # possible solution
                res = min(res, k)
                # try to decrease k
                right = k - 1
        return res
