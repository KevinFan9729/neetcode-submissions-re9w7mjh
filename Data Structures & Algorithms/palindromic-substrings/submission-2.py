class Solution:
    def countSubstrings(self, s: str) -> int:
        # we grow from the center
        # if we can grow from the center and we are palindrome then we have a found a Palindromic string
        # we need to be worry of even length Palindromic string
        # and odd length Palindromic string
        # grow can expand many steps. across all centers
        # Time O(n^2)
        # space O(1)
        count = 0
        def grow(left, right):
            nonlocal count
            while left >= 0  and right <= len(s)-1:
                if s[left] == s[right]:
                    count +=1
                    left-=1
                    right+=1
                else:
                    break

        
        for center in range(len(s)):
            # odd length Palindromic strings
            left = center - 1
            right = center + 1
            grow(left, right)

            # even length
            left = center
            right = center+1
            grow(left, right)

        count += len(s) # all characters are Palindromic
        return count