class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # max rate is the max of the pile
        # min rate is 1
        # we still need to simulate with a given k, how many hours are required to finish
        # if with a given k, we need more hours than h, we are too slow, k must be greater
        # if say with a given k, we need less hours than h, this h is valid k may be even smaller
        # we can binary search the k in range 1...max(piles)
        # Time O(n * log(max(piles)))
        # Space O(1)
        maxPile = max(piles)
        def hourRequired(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            return hours
        left, right = 1, maxPile
        mink = maxPile
        while left <= right:
            mid = left + (right-left)//2
            hourNeeded = hourRequired(mid)
            if hourNeeded > h:
                left = mid +1
            else:
                # this k is valid
                # but we may find a even smaller k
                mink = min(mink, mid)
                right = mid-1 

        return mink