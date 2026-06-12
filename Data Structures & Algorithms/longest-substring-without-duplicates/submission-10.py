class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # slding window?
        # grow while we are valid
        # and shrink when we are not 
        # we can use a hashset to check for duplicate?
        # xzyzxyz
        # Time O(n)
        # Space O(n)
        maxLen = 0
        wind = set()
        left = 0
        for right in range(len(s)):
            # we grow the window when there is no dup
            char = s[right]
        # adding char will case duplicate
            while char in wind:
                wind.remove(s[left])
                left +=1
            wind.add(char)
            winLen = right -left +1
            maxLen = max(winLen, maxLen)
        return maxLen
