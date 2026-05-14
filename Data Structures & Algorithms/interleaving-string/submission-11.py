class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # say we have p1 for s1 and p2 for s2 and p3 for s3
        # p3 = p1+p2 so we dont need p3 to track s3
        # at each step, check if s1 or s2 equal to s3
            # (p1, p2) means:
            # you have consumed s1[:p1]
            # you have consumed s2[:p2]
            # so you must be matching s3[p1 + p2] next
        # if only s1[p1] equal then p1 can be incremented
        # if only s2[p2] equal then p2 can be incremented
        # if they are all equal then need to try both
        # if none are equal then return false
        # Time O(n*m) # at most n*m states n is len(s1) m is len(s2)
        # Space O(n*m)
        if len(s1) + len(s2) != len(s3):
            return False
        memo = {}
        def compare(p1, p2):
            if (p1+p2) >= len(s3):
                return True
            if (p1,p2) in memo:
                return memo[(p1,p2)]

            s1Check = p1 < len(s1) and s3[p1+p2] == s1[p1]
            s2Check = p2 < len(s2) and s3[p1+p2] == s2[p2]

            tryS1 = False
            tryS2 = False
            if s1Check and not s2Check:
                tryS1 = compare(p1+1, p2)
            elif s2Check and not s1Check:
                tryS2 = compare(p1, p2+1)
            elif s1Check and s2Check:
                tryS1 = compare(p1+1, p2)
                tryS2 = compare(p1, p2+1)
            else:
                memo[(p1,p2)] = False
                return False
            ans = tryS1 or tryS2
            memo[(p1,p2)] = ans
            return ans

        return compare(0,0)