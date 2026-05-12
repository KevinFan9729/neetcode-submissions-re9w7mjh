class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # we need to track open bracket and close bracket
        # if say num of open cannot exceed num close bracket
        # otherwise will be invalid, say n =2
        # open = 2 # close = 1
        # ) <- not valid
        # we need to generate brackets
        # at each step we can decide
            # include a open
            # include a close
        # do this recursively
        # Time O(4^n) as the tharget is length of 2n, 2 choices each step, so 2^(2n)
        # Space O(n)
        curr = []
        res = []

        def gen(openB, closeB):
            if openB <0  or closeB < 0:
                return
            if openB > closeB:
                return
            if openB == 0  and closeB == 0:
                res.append("".join(curr[:]))
                return
            
            # include an open bracket
            curr.append("(")
            gen(openB-1, closeB)
            curr.pop()
            # include an close bracket
            curr.append(")")
            gen(openB, closeB-1)
            curr.pop()
        
        gen(n, n)
        return res


