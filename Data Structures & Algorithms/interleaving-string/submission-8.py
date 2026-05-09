class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # order of characters matter
        # 3 pointers?
        # say we have p1 p2 p3
        # if s1[p1] == s3[p3], increment p1 and p3
        # if s2[p2] == s3[p3], increment p2 and p3
        # if neither p1 nor p2 equal to p3, then return false
        # if they both matches, can s1[i:] and s2[j:] form s3[i+j:]?
        # probably dont need p3 anymore
        # at the end if p1 == len(s1) p2 == len(s2) return True
        # Time O(i+j)
        # Space O(i+j)
        if len(s1) + len(s2) != len(s3):
            return False
        memo = {}
        def canForm(i,j):
            if i == len(s1) and j == len(s2):
                return True
            if (i,j) in memo:
                return memo[(i,j)]
            tryI = False
            tryJ = False
            if i < len(s1) and s1[i] == s3[i+j]:
                tryI = canForm(i+1, j)
            if j < len(s2) and s2[j] == s3[i+j]:
                tryJ = canForm(i, j+1)
            memo[(i,j)] = tryI or tryJ
            return memo[(i,j)]
        
        res = canForm(0,0)
        return res
