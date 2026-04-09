class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointers
        # Time O(n)
        # Space O(n) due to the string construction
        check_str = "".join(char.lower() for char in s if char.isalnum())
        left, right = 0, len(check_str)-1
        while left <= right:
            if check_str[left] != check_str[right]:
                return False
            left+=1
            right-=1
            
        return True