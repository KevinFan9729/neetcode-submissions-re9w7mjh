class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        def expand_and_count(left, right):
            nonlocal count
            while left >=0 and right <= len(s)-1:
                if s[left] == s[right]:
                    count +=1
                else:
                    return
                left -= 1
                right +=1
        for mid in range(len(s)):
            expand_and_count(mid - 1, mid +1)
            expand_and_count(mid, mid+1)
        count += len(s) # all single characters are palindromic
        return count