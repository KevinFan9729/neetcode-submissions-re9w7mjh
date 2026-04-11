class Solution:
    def longestPalindrome(self, s: str) -> str:
        # we can grow the string from the middle
        # we have two types of middle
            # one characters in the middle
            # two characters in the middle
        # grow can be two pointers
        # Time O(n^2)
        # Space O(1)

        def grow(left, right):
            nonlocal maxLeft, maxRight, maxLen
            while left >=0 and right < len(s):
                if s[left] == s[right]:
                    currLen = right - left + 1
                    if maxLen < currLen:
                        maxLeft = left
                        maxRight = right
                        maxLen = currLen
                else:
                    break
                left-=1
                right+=1

        # case 1: only one character as mid
        maxLeft, maxRight = 0, 0
        maxLen = 1
        for mid in range(len(s)):
            left = mid -1
            right = mid +1
            grow(left, right)
            mid1 = mid
            mid2 = mid1+1
            if mid2 < len(s):
                if s[mid1]!=s[mid2]:
                    continue
                if maxLen <2:
                    maxLeft, maxRight = mid1, mid2
                    maxLen = 2
                left = mid1-1
                right = mid2+1
                grow(left, right)

            
        res = s[maxLeft:maxRight+1]
        return res
                