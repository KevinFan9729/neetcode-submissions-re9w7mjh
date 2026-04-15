class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # so order matters but we can remove (look over) an arbitrary number of character
        # recursive two pointer(states) i,j
        # when both char are the same, we can advance both i and j
        # if char are not the same, need to fix one and try the other
            # need to try both directions
        # the function return the longest common subsequence
        # Time O(m*n)
        # Space O(m*n)
        
        memo = {}
        def gen(i, j):
            if i >= len(text1) or j >=len(text2):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if text1[i] == text2[j]:
                same = 1 + gen(i+1,j+1)
                memo[(i,j)] = same
                return same
            else:
                tryT1 = gen(i+1, j)
                tryT2 = gen(i, j+1)
                longest = max(tryT1, tryT2)
                memo[(i,j)] = longest
                return longest
        res = gen(0,0)
        return res 