class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # for each character we can keep this character or we can remove this chracter
        # oh wait maybe we can start and both ends of the string
        # we just assume we have a palindrome (longest bascially means that we have a palindrome of len(s))
        # ccbbcca
        # if we find an offending character we try remove the left character and the right character
        # or try to remove both
        # if they agree, this means length +2 (two agreeing characters)
        # we can define a function which return the max Palindromic sequnce length
        # Time O(n^2)
        # space O(n^2)
        memo = {}
        def findMax(left, right):
            if left == right:
                return 1 # length of one character is one
            if left > right:
                # invalid
                return 0
            if (left, right) in memo:
                return memo[(left, right)]
            maxLen = 1
            if s[left] == s[right]:
                bothSame = 2 + findMax(left+1, right-1)
                maxLen = max(maxLen, bothSame)
            else:
                tryLeft = findMax(left+1, right)
                tryRight = findMax(left, right-1)
                maxLen = max(maxLen, tryLeft, tryRight)
            memo[(left, right)] = maxLen
            return maxLen

        res = findMax(0, len(s)-1)
        return res