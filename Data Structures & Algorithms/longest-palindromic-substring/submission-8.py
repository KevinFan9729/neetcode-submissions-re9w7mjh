class Solution:
    def longestPalindrome(self, s: str) -> str:
        # ok so every palindrome has a center
        # some palindrome's center is a single character
        # some other palindrome's center will be 2 characters (and they need to be the same)
        # abba
        # abbba
        # we can loop through the array linearly (or do two passes?)
        # then pick centers and then allow the center to "grow"
            # one path is to assume that the single character is a center
            # one path is to assume that 2 characters are center
        # Time O(n^2)
        # Space O(1)
        max_len = 0
        res = ""
        def _grow(left, right):
            nonlocal max_len, res
            while left >=0 and right < len(s):
                if s[left] == s[right]:
                    curr_len = right - left + 1
                    if max_len < curr_len:
                        max_len = curr_len
                        res = s[left:right+1]
                else:
                    break
                left-=1
                right+=1
        # check for the center is a single character
        for center_idx in range(len(s)):
            curr_len = 1
            if max_len < curr_len: # a single character is a valid palindrome
                max_len = curr_len
                res = s[center_idx]
            left = center_idx - 1
            right = center_idx + 1
            _grow(left, right)
            # check for the center has two characters
            center_idx1 = center_idx
            center_idx2 = center_idx + 1 if center_idx < len(s)-1 else -1
            print(center_idx2)
            if center_idx2 == -1 or s[center_idx1] != s[center_idx2]:
                continue
            # we already have a valid palindrome at this point
            curr_len = 2
            if max_len < curr_len:
                max_len = curr_len
                res = s[center_idx1:center_idx2+1]
            left = center_idx1 - 1
            right = center_idx2 + 1
            _grow(left, right)
        return res
                    
