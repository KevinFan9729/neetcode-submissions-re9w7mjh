class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # recursive solution
        # canForm(index1, index2, index3)
        # base if index3 >= len(s3) and index2 >= len(s2) and index1 >= len(s1): return True
        # base if s1[index1]!= s3[index3] and s2[index2]!= s3[index3] return False

        if len(s1) +len(s2) != len(s3):
            return False
        def canForm(index1, index2, index3):
            if index3 >= len(s3) and index2 >= len(s2) and index1 >= len(s1):
                return True
            if index1 < len(s1) and s1[index1] == s3[index3]:
                if canForm(index1+1, index2, index3+1):
                    return True
            if index2 < len(s2) and s2[index2] == s3[index3]:
                if canForm(index1, index2+1, index3+1):
                    return True
            return False
        ans = canForm(0,0,0)
        return ans