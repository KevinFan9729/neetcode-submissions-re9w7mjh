class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs(start_index):
            if start_index >= len(s): # run out of letters, all partitions are valid 
                res.append(part.copy())
                return
            for end_index in range(start_index, len(s)):
                # Check if s[start_index:end_index+1] is a palindrome
                if self.isPalindrome(s, start_index, end_index):
                    part.append(s[start_index : end_index + 1])
                    dfs(end_index + 1)
                    part.pop()
        dfs(0)
        return res

    def isPalindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left +=1
            right -=1
        return True