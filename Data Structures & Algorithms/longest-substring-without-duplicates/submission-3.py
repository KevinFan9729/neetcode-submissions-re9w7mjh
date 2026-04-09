class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        # The key operations (add to set, check for duplicate, and remove from set) 
        # for each character are performed a constant number of times.
        # O(n)
        l, r = 0, 0
        longest, length = 1, 1
        if not s:
            return 0
        charSet = set()
        while l <= r and r <len(s):
            charSet.add(s[r])
            if len(s[l:r+1]) != len(charSet): # detects a duplicate in the string
                duplicate_token = s[r]
                charSet.remove(duplicate_token)
                while l < r: #shrink the window
                    if s[l] != duplicate_token:
                        charSet.remove(s[l])
                        l += 1
                    else:
                        l += 1
                        break
            else:
                length = len(charSet)
                r += 1
            longest = max(longest, length)
                
        return longest

