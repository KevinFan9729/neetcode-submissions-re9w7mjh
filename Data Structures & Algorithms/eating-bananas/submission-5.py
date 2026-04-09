class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # we want the minium k (the banana eating rate)
        # h is at least equal to the number of piles (mentioned in the question)
            # due to this contraint "you may finish eating the pile but you can not eat from another pile in the same hour."
            # if h < len(piles), we do not have solution
        # k is an int
        # we know that at most k = max(piles)
        # at min k = 1 (say we have piles = [10, 20, 30], but h=999)
        # k now has a range 
        # how to check if k is good
        # loop through pile
        # each pile will need math.ceil(piles[i]/k) to finish
        # Time O(mlogM) m is the length of the piles and n is the M is the max(piles)
        # Space O(1)
        def kValid(k):
            # O(m)
            # if we know k 
            # at each pile we will use up time math.ceil(piles[i]/k)
            time = 0
            for i in range(len(piles)):
                time += math.ceil(float(piles[i])/k)
                if time > h:
                    return False
            return time <= h
        # k_range = list[range(1, max(piles))]
        # binary search
        left, right = 1, max(piles)
        k = -1
        while left <= right:
            mid = left + (right-left)//2
            valid = kValid(mid)
            if not valid:
                # k should be bigger
                left = mid +1
            else:
                # a potential k is found
                # try to find a even smaller k
                right = mid -1
                k = mid
        return k



