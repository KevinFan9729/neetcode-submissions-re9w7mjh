class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # permutation means the subtring order does not matter
        # but we need to have all characters and the count must be correct
        # sliding window with fixed size???
        # the window size must be the size of length of s1
        # Time O(n)
        # Space O(1)
        if len(s2) < len(s1):
            return False
        
        s1Map = {}
        windMap = {}
        for char in s1:
            if char not in s1Map:
                s1Map[char] = 0
            s1Map[char] += 1
        winSize = len(s1)
        # build the first winMap
        for char in s2[0:winSize]:
            if char not in windMap:
                windMap[char] = 0
            windMap[char] += 1

        if windMap == s1Map:
            return True
        leftIndx = 0
        for right in s2[winSize:]:
            # incoming char
            windMap[right] = windMap.get(right, 0) + 1
            # outgoing char
            left = s2[leftIndx]
            windMap[left] -=1
            if windMap[left] == 0:
                del windMap[left]
            leftIndx+=1
            if windMap == s1Map:
                return True
            
        return False