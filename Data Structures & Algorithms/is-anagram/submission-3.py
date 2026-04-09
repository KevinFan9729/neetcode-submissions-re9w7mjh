from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        smap = defaultdict(int)
        tmap = defaultdict(int)
        for i in range(len(s)):
            smap[s[i]] += 1
            tmap[t[i]] += 1
        return smap == tmap