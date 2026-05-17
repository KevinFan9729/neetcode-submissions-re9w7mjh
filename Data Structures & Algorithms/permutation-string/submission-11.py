class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # permutation means the subtring order does not matter
        # but we need to have all characters and the count must be correct
        # sliding window with fixed size???
        # the window size must be the size of length of s1
        # Time O(n*m)
        # Space O(n)
        if len(s2) < len(s1):
            return False
        
        s1Map = {}
        for char in s1:
            if char not in s1Map:
                s1Map[char] = 0
            s1Map[char] += 1
        winSize = len(s1)
        for start in range(len(s2)):
            end = start+winSize
            if end >= len(s2)+1:
                # at this point we do not have a window of size winSize
                return False
            winMap = s1Map.copy()
            for char in s2[start:end]:
                if char in winMap:
                    winMap[char]-=1
                    if winMap[char] == 0:
                        del winMap[char]
            if len(winMap) == 0:
                return True
            
        return False