class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window?
        # in the current window, how many characters are not the most frequent one
        # we can know which letter to replace by finding the non-majority character in the window
        # we need to keep track of a maxFreq -> max freq in the hashmap
        # Time O(n)
        # Space O(n)
        windowMap = defaultdict(int)
        left, right = 0,0
        maxLen = 0
        needToReplace = -1
        maxFreq = 0

        while right <= len(s)-1:
            if needToReplace <= k:
                # valid
                windowMap[s[right]]+=1
                maxFreq = max(maxFreq, windowMap[s[right]])
            else:
                # shrink the window
                while needToReplace > k:
                    windowMap[s[left]]-=1
                    if windowMap[s[left]] == 0:
                        del windowMap[s[left]]
                    left+=1
                    string = s[left:right+1]
                    needToReplace = right-left+1 - maxFreq
            needToReplace = right-left+1 - maxFreq
            string = s[left:right+1]
            if needToReplace <= k:
                maxLen = max(maxLen, right-left+1)
                right+=1
            
        return maxLen
    