class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # recursion with backtracking
        # needs two states
        # openN, closeN
        # openN cannot be more than closeN
        # i.e. openN= 1 closeN = 0
        # ( )) -> not valid
        # at every step,
        # 2 decsions
        # include the current bracket
        # include the close brakcet
        # Time O(2^(2n)*n) as each recursion step add one character 
        # Space O(n)

        res = []
        curr = []
        def gen(openN, closeN):
            if openN ==0 and closeN ==0:
                res.append("".join(curr))
                return
            if openN> closeN:
                return # invalid
            if openN <0 or closeN <0:
                return # invalid

            # include open
            curr.append("(")
            gen(openN-1, closeN)
            curr.pop()
            # include close
            curr.append(")")
            gen(openN, closeN-1)
            curr.pop()

        gen(n,n)
        return res
            