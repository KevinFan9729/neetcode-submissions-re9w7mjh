from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if the length of two strings are different, not anagram
        if len(s) != len(t):
            return False
        countS = defaultdict(int)
        countT = defaultdict(int)

        for i in range(len(s)):
            countS[s[i]] +=1
            countT[t[i]] +=1
        return countS == countT
