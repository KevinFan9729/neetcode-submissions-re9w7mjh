class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # O(n^2) solution
        l, r = 0, 0
        longest, length = 1, 1
        if not s:
            return 0
        charSet = set()
        for l in range(len(s)):
            while l <= r and r <len(s):
                charSet.add(s[r])
                if len(s[l:r+1]) != len(charSet): # detects a duplicate in the string
                    charSet.clear()
                    r = l+1
                    break
                else:
                    length = len(charSet)
                    r += 1
                longest = max(longest, length)
                
        return longest
