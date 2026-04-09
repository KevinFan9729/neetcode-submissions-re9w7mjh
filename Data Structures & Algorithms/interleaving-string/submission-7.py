class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # recursive solution. Three arguments index for s1, s2 and s3
        # base case if s3_idx >= len(s3) and s2_idx >= len(s2) and s1_idx >= len(s1), return True, we used up all characters and s3 can be constructed from s1 and s2
        # how to recurse?
            # if s1[s1_idx] == s3[s3_idx], increment s1_idx and s3_idx and recurse
            # if s1[s2_idx] == s3[s3_idx], increment s2_idx and s3_idx and recurse
        # if neither can be met, return False
        # O(m * n) time and space 

        if len(s1) + len(s2) != len(s3):
            return False

        memo = {}
        def canForm(s1_idx, s2_idx, s3_idx):
            if s3_idx >= len(s3) and s2_idx >= len(s2) and s1_idx >= len(s1):
                return True
            if (s1_idx, s2_idx) in memo:
                return memo[s1_idx, s2_idx]
            if s1_idx < len(s1) and s1[s1_idx] == s3[s3_idx]:
                if canForm(s1_idx+1, s2_idx, s3_idx +1):
                    memo[(s1_idx, s2_idx)] = True
                    return True
            if s2_idx < len(s2) and s2[s2_idx] == s3[s3_idx]:
                if canForm(s1_idx, s2_idx+1, s3_idx +1):
                    memo[(s1_idx, s2_idx)] = True
                    return True
            memo[(s1_idx, s2_idx)] = False
            return False
        
        ans = canForm(0,0,0)

        return ans