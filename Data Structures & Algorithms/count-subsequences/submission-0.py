class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # can we solve this recursively?
        # say the recursive function takes two indeces: indexS, indexT
        # if indexS and indexT matches we have two options
            # 1.we will incremenet both indexS and indexT, try to search the next character
            # 2.we will increment indexS only, this is try to see if we can have a new match despite the current match
        # if indexS and indexT does not match we will increment indexS and leave indexT as the same
        # base case:
            # if indexT >= len(t), we match all characters in t, we found a valid sequence, return 1
            # if indexT < len(T) and indexS >= len(s), we run out of charcaters in s but we still have 
            # characters in t, therefore, we cannot form a sequence, return 0
        # O(2^(m+n)) at most we will make 2 decsions at a step (i.e. when characters matches, include or exclude)
        # O(m+n) in space due to the call stack
        def countSeq(indexS, indexT):
            if indexT >= len(t):
                return 1
            if indexT < len(t) and indexS >= len(s):
                return 0
            
            if s[indexS] == t[indexT]:
                # 1.we will incremenet both indexS and indexT, try to search the next character
                include = countSeq(indexS+1, indexT+1)
                # 2.we will increment indexS only (skip the current character in s)
                exclude = countSeq(indexS+1, indexT)
                count = include + exclude
                return count
            else:
                count = countSeq(indexS+1, indexT)
                return count
        ans = countSeq(0,0)
        return ans 