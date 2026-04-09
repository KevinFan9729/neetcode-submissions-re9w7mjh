class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # O(m*n) each path is searched once
        # O(m*n) space, call stack is still O(m+n) but we have a hash map that can record all m*n possible outcomes 
        memo = {}
        def searchCompare(index1, index2):
            if index1 >= len(text1) or index2 >= len(text2):
                return 0
            if text1[index1] == text2[index2]:
                return searchCompare(index1+1, index2+1) + 1
            if (index1, index2) in memo:
                return memo[(index1, index2)]
            if text1[index1] != text2[index2]:
                searchTxt1 = searchCompare(index1+1, index2)
                searchTxt2 = searchCompare(index1, index2+1)
                maxLen = max(searchTxt1, searchTxt2)
                memo[(index1, index2)] = maxLen
                return maxLen
        ans = searchCompare(0,0)
        return ans

