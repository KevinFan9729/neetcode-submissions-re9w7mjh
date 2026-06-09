class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # number of characters to be replaced inside of a winodw
        # is equal to the size of the window - the majority character count
        # we use a hashmap to keep track of what are the characters inside of the window
        # sliding window
        # we will keep growing the window until the number we need to replaced is exceeding k
        # if that is the case, we will shrink the window
        # Time O(n)
        # Space O(1)
        maxLen = 1
        window = {}
        left, right = 0, 0
        def findMaxCount(window):
            maxCount = 0
            for char in window:
                maxCount = max(maxCount, window[char])
            return maxCount

        while right < len(s):
            # grow the window
            window[s[right]] = window.get(s[right], 0) + 1
            winLen = right - left + 1
            needReplace = winLen - findMaxCount(window)
            while needReplace > k:
                # we need to shrink the window
                window[s[left]] -= 1
                left += 1
                winLen = right - left + 1
                needReplace = winLen - findMaxCount(window)
            # now the window is valid
            winLen = right - left + 1
            maxLen = max(maxLen, winLen)
            right += 1

        return maxLen