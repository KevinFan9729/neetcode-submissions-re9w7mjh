class Solution:
    def countSubstrings(self, s: str) -> int:
        # isPal(l, r)
        # meaning:
        # whether s[l:r+1] is a palindrome
        # here we are reduing the palindrome
        # Time O(n^2)
        # Space O(n^2)
        memo = {}
        def isPal(l,r):
            if l >=r:
                # empty string, a single character are palindromes
                return True
            if s[l] != s[r]:
                return False
            if (l,r) in memo:
                return memo[(l,r)]
            
            res = isPal(l+1, r-1)
            memo[(l,r)] = res
            return res
        count = 0
        for l in range(len(s)):
            for r in range(l, len(s)):
                if isPal(l, r):
                    count += 1
        return count