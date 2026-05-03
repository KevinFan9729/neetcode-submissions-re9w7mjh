class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 1 to max(piles) is the range
        # binary search with simulation
        # Time O(nlog(max(piles)))
        # space O(1)
        def canFinish(k):
            hour = 0
            for pile in piles:
                curr = math.ceil(pile/k)
                hour += curr
                if hour > h:
                    return False
            return True
        
        left, right = 1, max(piles)

        while left < right:
            mid = left + (right-left)//2
            possible = canFinish(mid)
            if not possible:
                # this mid is not possible
                # k is in the right
                left = mid + 1
            else:
                # k can be in the left or mid
                right = mid
            
        return left