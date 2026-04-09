class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # two rules
            # we have n open parenthesis and n close parenthesis
            # we can only add a close parenthesis when open_count > close_count
        stack = []
        res = []

        def backtrack(open_count, close_count):
            if open_count == close_count == n: #stop
                res.append("".join(stack))
                return 
            if open_count < n:
                stack.append("(")
                backtrack(open_count+1, close_count)
                stack.pop()
            if open_count > close_count:
                stack.append(")")
                backtrack(open_count, close_count+1)
                stack.pop()
        backtrack(0, 0)
        return res

        