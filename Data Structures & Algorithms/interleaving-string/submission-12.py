class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # if their lengths do not agree, then impossible
        # the order of strings are very important
        # we can define a function that has 2 ptrs p1 p2
        # p3 is really p1+p2
        # if say either of the p1 is matching s3
        # then we increment the respective ptr
        # if neither of them matches then we know that we need to return false
        # if one of the pinter runs out, we will check the s3 with the remining ptr
        # Time O(n*m)
        # Space O(n*m)
        if len(s1)+len(s2) != len(s3):
            return False
        memo = {}
        def check(p1, p2):
            if p1 >= len(s1)  and p2 < len(s2):
                if s2[p2:] == s3[p1+p2:]:
                    return True
                return False
            if p1 < len(s1)  and p2 >= len(s2):
                if s1[p1:] == s3[p1+p2:]:
                    return True
                return False
            if p1>= len(s1) and p2>= len(s2):
                return True
            if (p1, p2) in memo:
                return memo[(p1, p2)]

            if s1[p1] != s3[p1+p2] and s2[p2] != s3[p1+p2]:
                return False
            trys1 = False
            trys2 = False
            if s1[p1] == s3[p1+p2] and s2[p2] == s3[p1+p2]:
                trys1 = check(p1+1,p2)
                trys2 = check(p1, p2+1)
            elif s1[p1] == s3[p1+p2] and s2[p2] != s3[p1+p2]:
                trys1 = check(p1+1, p2)
            elif s1[p1] != s3[p1+p2] and s2[p2] == s3[p1+p2]:
                trys2 = check(p1, p2+1)

            res = trys1 or trys2
            memo[(p1,p2)] = res
            return res

        res = check(0,0)
        return res