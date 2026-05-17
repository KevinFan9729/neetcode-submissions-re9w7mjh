class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # sliding window?
        # we will increase the window until we have more than k distinct characters
        # then we will shrink the window
        # Time O(n)
        # Sapce O(n)
        winCount = defaultdict(int)
        left = 0
        maxLen = 0
        for right in range(len(s)):
            winCount[s[right]] +=1
            distinctCount = len(winCount)
            while distinctCount > k:
                winCount[s[left]] -= 1
                if winCount[s[left]] == 0:
                    del winCount[s[left]]
                left+=1
                distinctCount = len(winCount)
            winLen = right - left + 1
            maxLen = max(maxLen, winLen)
        return maxLen