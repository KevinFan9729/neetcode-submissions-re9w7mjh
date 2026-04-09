class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # use two pointers to do inpalce swapping
        # Time O(n)
        # Space O(1)

        left, right = 0, len(s)-1

        while left < right:
            temp = s[right]
            s[right] = s[left]
            s[left] = temp
            # or just do in python
            # s[left], s[right] = s[right], s[left]
            left+=1
            right-=1
