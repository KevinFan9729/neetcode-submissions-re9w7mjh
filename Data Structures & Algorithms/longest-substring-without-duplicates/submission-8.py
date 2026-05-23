class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # slding window with a hash set?
        # if the item does not exists in the set, add it to set and increase the window
        # if we have duplicate, keep shrinking the window from the left
        # zxyzxyz
        # xzyzxyz
        # Time O(n)
        # Space O(n)
        maxLen = 0
        left = 0
        seen = set()
        for right in range(len(s)):
            if s[right] not in seen:
                seen.add(s[right])
            else:
                # s[right] will casue a duplicate
                while True:
                    seen.remove(s[left])
                    left+=1
                    if s[right] not in seen:
                        seen.add(s[right])
                        break
            length = right - left +1
            maxLen = max(maxLen, length)
        
        return maxLen