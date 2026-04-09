class Solution:
    def countSubstrings(self, s: str) -> int:
        # Memoization cache
        memo = {}
        count = 0
        def is_palindrome(l: int, r: int) -> bool: # srart at both ends
            if l >= r:
                return True
            if (l, r) in memo:
                return memo[(l, r)]
            if s[l] == s[r]:
                memo[(l, r)] = is_palindrome(l + 1, r - 1)
                return memo[(l, r)]
            memo[(l, r)] = False
            return False
        
        def expand_and_count(l: int, r: int) -> None:
            nonlocal count
            if l >= 0 and r < len(s) and is_palindrome(l, r):
                count +=1
                expand_and_count(l - 1, r + 1)
        
        for i in range(len(s)):
            expand_and_count(i, i)        # Odd length palindromes
            expand_and_count(i, i + 1)    # Even length palindromes
        return count