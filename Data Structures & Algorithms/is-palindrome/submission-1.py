class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer
        # we have str.isalnum() as a method which we can check if the string is alphanumeric
        # we can sanitize the string (remove white space, only have alphanumeric char, and lower)
        # then just have two pointer left and right to check 
        # Time O(n)
        # Space O(n) bec of the string we constructed

        clean = "".join(char for char in s if char.isalnum())
        clean = clean.lower()

        left = 0
        right = len(clean) - 1

        while left < right:
            if clean[left] != clean[right]:
                return False
            left += 1
            right -= 1
        return True