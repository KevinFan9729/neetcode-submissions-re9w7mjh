from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sliding window
        # O(26 n)
        # O(n)
        if len(s1) > len(s2):
            return False
        L, R = 0, len(s1) - 1
        s1_map = defaultdict(int)
        s2_map = defaultdict(int)
        for char in s1:
            s1_map[char]+=1
        for char in s2[L:R+1]:
            s2_map[char]+=1
        while L <= R and R < len(s2):
            tmp = s2[L:R+1]
            if s1_map == s2_map: # at most 26 characters O(26)
                return True
            s2_map[s2[L]]-=1
            if s2_map[s2[L]] == 0:
                del s2_map[s2[L]]
            L += 1
            R += 1
            if R < len(s2):
                s2_map[s2[R]]+=1
            
        return False