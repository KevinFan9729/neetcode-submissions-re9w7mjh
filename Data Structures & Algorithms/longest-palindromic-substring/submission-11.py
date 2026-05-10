class Solution:
    def longestPalindrome(self, s: str) -> str:
        # we can start with a mid then expand outward with 2 pointers
        # mid can be one character in length
        # or 2 characters in length
        # Time O(n^2)
        # Space O(1) if not counting making the string
        def expand(startLeft, startRight):
            left, right = startLeft, startRight
            while left >=0 and right < len(s):
                if s[left] == s[right]:
                    left -= 1
                    right +=1
                else:
                    # left and right are invalid, return the previous valid ones
                    return (left+1, right-1)
            return (left+1, right-1)
        
        oddLen = 1
        oddStr = s[0]
        # mid is length of 1
        for mid in range(1, len(s)-1):
            startLeft, startRight = mid-1, mid+1
            left, right = expand(startLeft, startRight)
            length =  right-left + 1
            if oddLen < length:
                oddLen = length
                oddStr = s[left: right+1]
        evenLen = 0
        evenStr = ""
        # mid is length of 2:
        for mid in range(len(s)-1):
            if s[mid] == s[mid+1]:
                if evenLen < 2:
                    evenLen = 2
                    evenStr = s[mid:mid+2]
                startLeft, startRight = mid-1, mid+2
                left, right = expand(startLeft, startRight)
                length =  right-left + 1
                if evenLen < length:
                    evenLen = length
                    evenStr = s[left: right+1]
        
        return oddStr if oddLen > evenLen else evenStr