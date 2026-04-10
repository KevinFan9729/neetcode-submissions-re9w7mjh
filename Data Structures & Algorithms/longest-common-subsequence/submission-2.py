class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # recursion#
        # Time O(n^2)
        # Space O(n^2)
        memo = {}
        def compareGen(i,j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if text1[i] == text2[j]:
                return 1 + compareGen(i+1, j+1)
            else:
                # if they are not the same, we need to search
                advance_1 = compareGen(i+1, j)
                advance_2 = compareGen(i, j+1)
                max_len = max(advance_1, advance_2)
                memo[(i,j)] = max_len
                return max_len

        return compareGen(0,0)