class Solution:
    def longestPalindrome(self, s: str) -> str:
        # a single character is a palindrome
        # we can start at the mid and try to grow the window to get a larger palindrome
        # O(n^2) in time
        # O(1) in space
        maxLen = float("-inf")
        res = s[0]

        def grow(left, right): #O(n)
            while left >= 0 and right <= len(s)-1:
                nonlocal maxLen, res
                if s[left] == s[right]: # palindrome
                    length = right - left + 1
                    if maxLen < length:
                        maxLen = length
                        res = s[left: right+1]
                    left-=1
                    right+=1
                else:
                    return
        for mid in range(len(s)): #O(n)
            grow(mid-1, mid+1) # odd length string
            grow(mid, mid+1) # even length string
        return res
        