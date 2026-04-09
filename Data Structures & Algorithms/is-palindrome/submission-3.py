class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointers
        # Time O(n)
        # Space O(1)
        left, right = 0, len(s)-1
        while left <= right:
            if not s[left].isalnum():
                left +=1 # skip invalid characters
                continue
            if not s[right].isalnum():
                right -=1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left+=1
            right-=1
            
        return True