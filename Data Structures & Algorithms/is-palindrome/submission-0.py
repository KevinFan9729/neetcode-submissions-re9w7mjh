class Solution:
    def isPalindrome(self, s: str) -> bool:
        # O(n)
        cleanstr = filter(str.isalnum, s)
        cleanstr = "".join(cleanstr)
        cleanstr = cleanstr.lower()
        left, right = 0, len(cleanstr)-1
        while left < right:
            if cleanstr[left] != cleanstr[right]:
                return False
            left +=1
            right -=1
        return True
        