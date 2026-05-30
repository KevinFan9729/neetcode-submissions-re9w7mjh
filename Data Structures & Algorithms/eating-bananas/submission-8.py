class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # the range of k is 1 to max(piles)
        # w need a simulate method
        # canFinish(k)
        # this just go through all piles and bascially check if we can finish or not
        # if we cannot finish we need a bigger k
        # if we can finish, we may find a even smaller k
        # so we can do this the binary search way
        # Time O(nlogma)
        # Space o(1)

        # canFinish

        def canFinish(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
                if hours > h:
                    return False
            return True

        left, right = 1, max(piles)

        while left < right:
            mid = left + (right - left)//2
            finish = canFinish(mid)
            if not finish:
                left = mid + 1
            else:
                # k can maybe mid or even smaller"
                right = mid
            
        return left