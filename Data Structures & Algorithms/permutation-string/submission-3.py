from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sliding window
        if len(s1) > len(s2):
            return False
        L, R = 0, len(s1) - 1
        s1_map = defaultdict(int)
        for char in s1:
            s1_map[char]+=1
        res = True
        while L <= R and R < len(s2): # O(n)
            tmp = s2[L:R+1]
            tmp_map = s1_map.copy()
            for char in tmp:
                res = True
                if tmp_map.get(char) is not None:
                    tmp_map[char] -= 1
                    if tmp_map[char] < 0:
                        res = False
                        break
                else:
                    res = False
                    break
            if res: # early stopping 
                return res
            L += 1
            R += 1
        return res