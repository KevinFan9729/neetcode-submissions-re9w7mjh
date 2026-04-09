class Solution:
    def validPalindrome(self, s: str) -> bool:
        # check palindrome but with an extra life?
        # after we encounter a mistmatch, we need to 
        # decide if left or the right substring are Palindrome
        # need to check both side
        # two pointers
        # Time O(n)
        # Space O(1)
        def PurePalindrome(s: str, left = None, right = None):
            if left == None:
                left = 0
            if right == None:
                right = len(s)-1
            while left <=right:
                if s[left] != s[right]:
                    return (left, right)
                left+=1
                right-=1
            return True
        pureCheck = PurePalindrome(s)
        if pureCheck == True:
            return True
        else:
            left_break, right_break = pureCheck
            # check to remove the left offending character:
            leftCheck = PurePalindrome(s, left_break+1, right_break)
            if leftCheck == True:
                return True
            # check to remove the right offending character:
            rightCheck = PurePalindrome(s, left_break, right_break-1)
            if rightCheck == True:
                return True
        return False
            
            