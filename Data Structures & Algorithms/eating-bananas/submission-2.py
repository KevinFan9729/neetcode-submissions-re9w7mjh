import math
class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        piles = sorted(piles)
        k_range = range(1, piles[-1]+1)
        left = 0
        right = len(k_range) - 1
        res = float('inf')
        #O(nlogn)
        while left <= right:
            mid = left + (right - left)//2
            k = k_range[mid]
            tmp_hour = 0
            for i in piles:
                tmp_hour+= math.ceil(i/k)
            if tmp_hour > h: # rate is too slow, must increase k
                left = mid + 1
            else: # possible solution
                res = min(res, k)
                # try to decrease k
                right = mid - 1
        return res
