class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window
        # we need to compute the length of the window
        # and numToReplace = winLen - most frequnet char length
        # use a hashmap to track char count
        # and looping through the hashmap to find the most frequent count O(26) as we have only upper case english char
        # expand the window
            # but when numToReplace > k:
            # shrink the window
        # Time O(n)
        # Space O(1)
        left = 0
        count = defaultdict(int)

        def findMax(count):
            maxVal = 0
            for val in count.values():
                maxVal = max(val, maxVal)
            return maxVal
        maxLen = 1
        for right in range(len(s)):
            count[s[right]] +=1
            winLen = right- left + 1
            numToRep = winLen - findMax(count)
            while numToRep > k:
                count[s[left]] -=1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1
                winLen = right- left + 1
                numToRep = winLen - findMax(count)
            # at this point the winLen is valid
            maxLen = max(maxLen, winLen)
        return maxLen