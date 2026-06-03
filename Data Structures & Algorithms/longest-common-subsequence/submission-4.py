class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # define a function that return longest common subsequence length between text1[p1:] and text2[p2:]
        # we can have two pointer p1, p2
        # Time O(n*m)
        # Space O(n*m)
        memo = {}
        def findMax(p1, p2):
            if p1 >= len(text1) or p2 >= len(text2):
                # no longer valid
                return 0
            if (p1,p2) in memo:
                return memo[(p1,p2)]
            maxLen = 0
            if text1[p1] == text2[p2]:
                maxLen = max(maxLen, 1 + findMax(p1+1, p2+1))
            else:
                tryP1 = findMax(p1+1, p2)
                tryP2 = findMax(p1, p2+1)
                maxLen = max(maxLen, tryP1, tryP2)
            memo[(p1,p2)] = maxLen
            return maxLen

        res = findMax(0,0)

        return res