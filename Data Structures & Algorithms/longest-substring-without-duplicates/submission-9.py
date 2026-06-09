class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # slding window?
        # grow while we are valid
        # and shrink when we are not 
        # we can use a hashset to check for duplicate?
        # xzyzxyz
        # Time O(n)
        # Space O(n)
        left, right = 0, 0
        maxLen = 0
        dupCheck = set()
        while right <= len(s) -1:
            c = s[right] # this is a char we about to add
            # if c is not conflicting (i.e. not casue a duplicate, we will increase our window)
            while c in dupCheck:
                dupCheck.remove(s[left])
                left += 1
            dupCheck.add(c)
            maxLen = max(maxLen, right-left+1)
            right += 1
                
        return maxLen