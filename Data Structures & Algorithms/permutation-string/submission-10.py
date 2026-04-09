from collections import Counter
import copy
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # hmmm hashmap?
        # permutation means s1 and s2 have the same characters. order does not matter
        # we always check if s2 contains a permutation of s1 (stated in the question)
        # but one detail of the question is that the s2's substring must contain permutation of s1
        # substring means the characters must be continous
        # sliding window?
        # now we know the window size needs to be the length of s1
        # we just need to slide in s2 one item at the time
        # we add one char and remove one char in the window
        # so we "slide" the window by 1 each step

        # TIme O(m) where m is the length of s2
        # Space O(1) # only 26 characters

        n, m = len(s1), len(s2)
        if n > m:
            return False

        target = Counter(s1)
        window = Counter(s2[:n])
        
        if window == target:
            return True
    
        for i in range(n, m):
            # item entering the window
            window[s2[i]] += 1
            # item leaving the window
            window[s2[i-n]] -= 1

            if window[s2[i-n]] == 0:
                del window[s2[i-n]]
            
            if target == window:
                return True
            
        return False