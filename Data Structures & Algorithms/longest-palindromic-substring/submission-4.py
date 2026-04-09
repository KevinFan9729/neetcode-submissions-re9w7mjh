from collections import defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> str:
        Palindrome_Map = defaultdict(list)
        max_length = 1
        if len(s) == 1:
            return s
        Palindrome_Map[max_length].append(s[0])

        def genPalindromeStr(left, right):
            nonlocal max_length
            
            while left>=0 and right<= len(s) - 1:
                if s[left] == s[right]:
                    length = right - left + 1
                    max_length = max(max_length, length)
                    Palindrome_Map[length].append(s[left:right+1])
                    left -= 1
                    right += 1
                else:
                    break

        for mid in range(len(s)):
            genPalindromeStr(mid -1, mid +1)
            genPalindromeStr(mid, mid +1)
        
        return Palindrome_Map[max_length][0]